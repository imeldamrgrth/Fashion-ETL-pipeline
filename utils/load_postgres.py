from sqlalchemy import create_engine


def save_to_postgres(df):

    try:

        engine = create_engine(
            "postgresql+psycopg2://postgres:postgres@localhost:5432/fashion_db"
        )

        df.to_sql(
            "fashion_products",
            engine,
            if_exists="replace",
            index=False
        )

        print("Data loaded to PostgreSQL")

    except Exception as e:

        print("Error loading PostgreSQL:", e)