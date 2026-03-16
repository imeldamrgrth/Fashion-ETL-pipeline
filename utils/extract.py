import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def scrape_products():

    all_products = []

    for page in range(1, 51):

        print(f"Scraping halaman {page}")

        page_data = scrape_main(page)

        all_products.extend(page_data)

    df = pd.DataFrame(all_products)

    return df

def safe_text(element, selector=None):
    try:
        if selector:
            el = element.select_one(selector)  # Perbaikan di sini
        else:
            el = element
        return el.text.strip() if el else None
    except Exception:
        return None

def scrape_main(page=1):
    if page == 1:
        url = "https://fashion-studio.dicoding.dev/"
    else:
        url = f"https://fashion-studio.dicoding.dev/page{page}"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Halaman {page} gagal diakses, status {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.select("div.collection-card")

    from datetime import datetime
    timestamp = datetime.now().isoformat()
    results = []

    for card in cards:
        try:
            title = safe_text(card, "h3.product-title")
            price = safe_text(card, "div.price-container span.price")

            rating_p = None
            for p in card.find_all("p"):
                if p and p.text and "Rating:" in p.text:
                    rating_p = p.text.replace("Rating: ", "").strip()
                    break

            colors_p = None
            for p in card.find_all("p"):
                if p and p.text and ("Color" in p.text or "Colors" in p.text):
                    colors_p = p.text.replace("Colors: ", "").replace("Color: ", "").strip()
                    break

            size_p = None
            for p in card.find_all("p"):
                if p and p.text and "Size" in p.text:
                    size_p = p.text.replace("Size: ", "").strip()
                    break

            gender_p = None
            for p in card.find_all("p"):
                if p and p.text and "Gender" in p.text:
                    gender_p = p.text.replace("Gender: ", "").strip()
                    break

            results.append({
                "Title": title,
                "Price": price,
                "Rating": rating_p,
                "Colors": colors_p,
                "Size": size_p,
                "Gender": gender_p,
                "timestamp": timestamp
            })
        except Exception as e:
            print(f"Error parsing produk di halaman {page}: {e}")

    return results
