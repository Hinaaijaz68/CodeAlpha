import pandas as pd

# Load the dataset
df = pd.read_csv("books_dataset.csv")

# Display the first 5 rows
print("First 5 rows:")
print(df.head())

# Display number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns)

# Display data types
print("\nData types:")
print(df.dtypes)

# Display basic information
print("\nDataset information:")
df.info()
# Basic statistical analysis
print("\nStatistical Summary:")
print(df.describe())

# Average price
print("\nAverage book price:")
print(df["Price"].mean())

# Minimum price
print("\nCheapest book price:")
print(df["Price"].min())

# Maximum price
print("\nMost expensive book price:")
print(df["Price"].max())

# Average rating
print("\nAverage book rating:")
print(df["Rating"].mean())

# Number of books for each rating
print("\nNumber of books by rating:")
print(df["Rating"].value_counts().sort_index())
# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Check for duplicate book titles
print("\nNumber of duplicate book titles:")
print(df["Title"].duplicated().sum())

# Check price and rating ranges
print("\nPrice range:")
print(df["Price"].min(), "to", df["Price"].max())

print("\nRating range:")
print(df["Rating"].min(), "to", df["Rating"].max())
import matplotlib.pyplot as plt

# 1. Rating Distribution
plt.figure()
df["Rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

# 2. Price Distribution
plt.figure()
df["Price"].plot(kind="hist", bins=10)
plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# 3. Price vs Rating
plt.figure()
plt.scatter(df["Rating"], df["Price"])
plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig("price_vs_rating.png")
plt.show()

# Correlation between price and rating
correlation = df["Price"].corr(df["Rating"])

print("\nCorrelation between Price and Rating:")
print(correlation)