from src.scrape import scrape_books
from src.clean import clean_books
from src.load import load_books

if __name__ == "__main__":
    print("Scraping...")
    scrape_books()
    print("Cleaning...")
    clean_books()
    print("Loading to DB...")
    load_books()
    print("Pipeline complete!")
