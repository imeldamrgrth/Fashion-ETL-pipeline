# Fashion ETL Pipeline

## Overview

This project implements an **ETL pipeline** to collect fashion product data from a website, clean and transform the dataset, and store the results in both **CSV files** and a **PostgreSQL database**.

---

## Data Source

Data is scraped from:

https://fashion-studio.dicoding.dev/

The dataset includes information about fashion products such as:

* Product Name
* Price
* Rating
* Colors
* Size
* Gender
* Timestamp

---

## Tech Stack

* Python
* BeautifulSoup
* Pandas
* PostgreSQL
* SQLAlchemy
* Pytest
* Pytest-Cov

---

## Project Structure

```
fashion-etl-pipeline

├── tests
│   ├── conftest.py
│   ├── test_extract.py
│   ├── test_load.py
│   ├── test_postgres.py
│   └── test_transform.py
│
├── utils
│   ├── extract.py
│   ├── transform.py
│   ├── load_csv.py
│   └── load_postgres.py
│
├── main.py
├── products.csv
├── requirements.txt
└── README.md
```

---

## How to Run the Pipeline

1. Clone the repository

```
git clone
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the ETL pipeline

```
python main.py
```

---

## Running Tests

Run unit tests with coverage:

```
pytest --cov=utils
```

Current coverage: **86%**

---

## Output

The pipeline produces:

* Clean dataset stored as CSV
* Data loaded into PostgreSQL database
