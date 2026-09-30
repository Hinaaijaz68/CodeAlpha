# CodeAlpha Task 3: Data Visualization
# Dataset: Books to Scrape
# Libraries: Pandas and Matplotlib

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books_dataset.csv")
df.columns = df.columns.str.strip()

df["Price"] = (
    df["Price"].astype(str)
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

os.makedirs("visualizations", exist_ok=True)

print("CODEALPHA TASK 3: DATA VISUALIZATION")
print("-----------------------------------")
print("Total books:", len(df))
print("Average book price:", round(df["Price"].mean(), 2))
print("\nBooks by rating:")
print(df["Rating"].value_counts().sort_index())

# Graph 1: Number of books by rating
rating_counts = df["Rating"].value_counts().sort_index()
rating_counts.plot(kind="bar", edgecolor="black")
plt.title("Number of Books by Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visualizations/books_by_rating.png")
plt.show()
plt.close()

# Graph 2: Distribution of book prices
plt.hist(df["Price"].dropna(), bins=10, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Book Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("visualizations/book_price_distribution.png")
plt.show()
plt.close()

# Graph 3: Percentage of books by rating
rating_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Percentage of Books by Rating")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/books_rating_pie.png")
plt.show()
plt.close()

print("\nTask 3 visualizations completed successfully!")
print("Check the visualizations folder for your three graphs.")
