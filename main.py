from utils.extract import scrape_products
from utils.transform import transform_data
from utils.load_csv import save_to_csv
from utils.load_postgres import save_to_postgres


def main():

    print("Starting ETL pipeline...")

    raw_data = scrape_products()

    print("RAW DATA:", raw_data.shape)

    clean_data = transform_data(raw_data)

    save_to_csv(clean_data)

    save_to_postgres(clean_data)

    print("ETL Pipeline Finished")


if __name__ == "__main__":
    main()