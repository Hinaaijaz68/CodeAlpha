import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

# Scrape 10 pages
for page in range(1, 11):

    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping page {page}...")

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    for book in soup.select("article.product_pod"):

        title = book.h3.a["title"]

        price = book.select_one(".price_color").text

        rating = book.select_one("p.star-rating")["class"][1]

        availability = book.select_one(".availability").text.strip()

        book_url = "https://books.toscrape.com/" + book.h3.a["href"].replace("../", "") 

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "URL": book_url
        })


# Create DataFrame
df = pd.DataFrame(books)

# Clean Price
df["Price"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
    .astype(float)
)

# Convert Rating words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Remove duplicate books
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv("books_dataset.csv", index=False)

print("\nScraping completed successfully!")
print("Total books collected:", len(df))
print("Dataset saved as books_dataset.csv")