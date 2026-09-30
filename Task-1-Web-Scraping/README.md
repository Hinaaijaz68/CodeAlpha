# CodeAlpha Task 1 - Web Scraping

## Project Title

**Web Scraping of Books Data Using Python**

## Objective

The objective of this project is to collect book information from a public webpage using Python web scraping techniques and create a structured dataset.

## Website Used

**Books to Scrape**

The project collects book information from multiple pages of the website.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Visual Studio Code

## Data Collected

The following information was collected:

- Book Title
- Price
- Rating
- Availability
- Book URL

## Web Scraping Process

The project follows these steps:

1. Send a request to the website using the Requests library.
2. Retrieve the HTML content of each webpage.
3. Parse the HTML using BeautifulSoup.
4. Find the required book information from the HTML structure.
5. Extract the title, price, rating, availability, and URL.
6. Repeat the process for 10 pages.
7. Store the collected information in a Pandas DataFrame.
8. Clean the price and rating values.
9. Remove duplicate records.
10. Save the final dataset as a CSV file.

## Dataset

The scraper collected **200 books from 10 pages**.

The final dataset is stored in:

`books_dataset.csv`

## Dataset Columns

| Column | Description |
|---|---|
| Title | Name of the book |
| Price | Price of the book |
| Rating | Book rating from 1 to 5 |
| Availability | Availability status |
| URL | Complete URL of the book |

## Example Data

| Title | Price | Rating | Availability |
|---|---:|---:|---|
| A Light in the Attic | 51.77 | 3 | In stock |
| Tipping the Velvet | 53.74 | 1 | In stock |
| Soumission | 50.10 | 1 | In stock |
| Sharp Objects | 47.82 | 4 | In stock |

## Project Files

```text
CodeAlpha_WebScraping/
│
├── webscraping.py
├── books_dataset.csv
└── README.md