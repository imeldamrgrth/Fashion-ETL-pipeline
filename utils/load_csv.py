def save_to_csv(df):

    try:

        df.to_csv("products.csv", index=False)

        print("Data saved to CSV")

    except Exception as e:

        print("Error saving CSV:", e)