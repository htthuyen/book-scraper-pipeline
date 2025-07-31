# 📚 Book Scraper Pipeline

This project demonstrates a simple data engineering pipeline that extracts book data from [Books to Scrape](http://books.toscrape.com/), transforms it, and loads it into a SQLite database.

---

## 🚀 Project Overview

**Goal:** Build a basic ETL pipeline using Python to:
- 🧩 **Extract** book data (title, price, rating) via web scraping
- 🧼 **Transform** the data (clean/format it using pandas)
- 🏗️ **Load** it into a SQLite database

---

## 🛠️ Tech Stack

| Task         | Tools Used           |
|--------------|----------------------|
| Scraping     | `requests`, `BeautifulSoup` |
| Transformation | `pandas` |
| Storage      | `SQLite` (`sqlite3`) |
| Environment  | `virtualenv` + `pip` |

---

## 📁 Project Structure
book-scraper-pipeline/
├── data/                  # store raw or cleaned data
├── src/                   # all Python code goes here
│   ├── scrape.py
│   ├── clean.py
│   └── load.py
├── main.py                # runs the full pipeline
├── requirements.txt
└── README.md

---

## 📦 Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/htthuyen/book-scraper-pipeline.git
cd book-scraper-pipeline
```
### 2. Create and activate a virtual environment
```
python -m venv myenv
source myenv/bin/activate
```
### 3. Install dependencies
```
pip install -r requirement.txt
```

## 🧪 How to Run the Pipeline
```
python main.py
```

