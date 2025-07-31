import pandas as pd

def clean_books():
    df = pd.read_csv("data/books_raw.csv")

    #convert price to float
    df["Price"] = df["Price"].str.replace("Â£","").astype(float)

    #convert rating text to numeric
    rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}
    df["Rating"] = df["Rating"].map(rating_map)

    df.to_csv("data/books_clean.csv", index=False)