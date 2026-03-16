from utils.extract import scrape_products


def test_extract():

    df = scrape_products()

    assert df is not None