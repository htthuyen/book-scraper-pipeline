import pandas as pd
import sqlite3

def load_books():
    df = pd.read_csv("data/books_clean.csv")
    #connect to a new (or existing) SQLite db
    conn = sqlite3.connect("boooks.db") 
    df.to_sql("books", conn, if_exists="replace", index=False)
    conn.close()