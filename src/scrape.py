# to send HTTP requests to websites
import requests
#tp parse HTML and extract information from websites
from bs4 import BeautifulSoup
import csv

def scrape_books():
    #site link to scrape
    url = "http://books.toscrape.com/"
    #get request response
    response = requests.get(url)
    #parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    #find all book entries on the page, each book is wrapped in an <article class=
    books = soup.find_all("article", class_="product_pod")

    # an empty list to store scraped data
    data = []

    for book in books:
        #extraxt book title from inside the <h3><a> tag's title attribute
        title = book.h3.a["title"]
        #find the price inside a <p class="price_color">
        price = book.find("p", class_="price_color").text.strip()
        rating = book.p["class"][1]
        #store scraped data
        data.append((title, price, rating))

    with open("data/books_raw.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Rating"])
        writer.writerows(data)
