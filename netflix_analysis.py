# =====================================================
# NETFLIX DATA ANALYSIS PROJECT
# Author : Priya Gangone
# =====================================================

# ==========================
# Import Libraries
# ==========================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("data/netflix_titles.csv")

print("=" * 50)
print("NETFLIX DATA ANALYSIS")
print("=" * 50)

# ==========================
# Data Understanding
# ==========================

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nDataset Information")
df.info()

print("\nMissing Values")
print(df.isnull().sum())

print("\nMissing Value Percentage")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)

print("\nDuplicate Rows")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# ==========================
# Data Cleaning
# ==========================

# Fill missing values in Rating
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

# Fill missing values in Duration
df["duration"] = df["duration"].fillna(df["duration"].mode()[0])

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# =====================================================
# EDA QUESTION 1
# Movies vs TV Shows
# =====================================================

type_counts = df["type"].value_counts()

print("\nMovies vs TV Shows")
print(type_counts)

type_counts.plot(kind="bar", figsize=(6,4))

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.savefig("images/movies_vs_tvshows.png")

plt.show()


# =====================================================
# EDA QUESTION 2
# Top 10 Countries
# =====================================================

country_counts = df["country"].value_counts().head(10)

print("\nTop 10 Countries")
print(country_counts)

country_counts.plot(kind="bar", figsize=(10,5))

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.savefig("images/top_10_countries.png")

plt.show()


# =====================================================
# EDA QUESTION 3
# Release Year Analysis
# =====================================================

year_counts = df["release_year"].value_counts().sort_index()

print("\nContent Released by Year")
print(year_counts)

year_counts.plot(kind="line", figsize=(10,5))

plt.title("Netflix Content Released by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True)

plt.savefig("images/release_year_trend.png")

plt.show()

print("\nHighest Release Year")
print("Year :", year_counts.idxmax())
print("Titles :", year_counts.max())

# =====================================================
# EDA QUESTION 4
# Ratings Distribution
# =====================================================

rating_counts = df["rating"].value_counts()

print("\nRatings Distribution")
print(rating_counts)

rating_counts.plot(kind="bar", figsize=(10,5))

plt.title("Netflix Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.savefig("images/ratings_distribution.png")

plt.show()


# =====================================================
# EDA QUESTION 5
# Top 10 Genres
# =====================================================

genres = df["listed_in"].str.split(",")
genres = genres.explode()
genres = genres.str.strip()

genre_counts = genres.value_counts().head(10)

print("\nTop 10 Genres")
print(genre_counts)

genre_counts.plot(kind="bar", figsize=(12,5))

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.savefig("images/top_10_genres.png")

plt.show()


# =====================================================
# EDA QUESTION 6
# Top 10 Directors
# =====================================================

director_counts = df["director"].dropna().value_counts().head(10)

print("\nTop 10 Directors")
print(director_counts)

director_counts.plot(kind="bar", figsize=(12,5))

plt.title("Top 10 Directors on Netflix")
plt.xlabel("Director")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.savefig("images/top_10_directors.png")

plt.show()

# =====================================================
# EDA QUESTION 7
# Top 10 Actors
# =====================================================

actors = df["cast"].dropna().str.split(",")
actors = actors.explode()
actors = actors.str.strip()

actor_counts = actors.value_counts().head(10)

print("\nTop 10 Actors")
print(actor_counts)

actor_counts.plot(kind="bar", figsize=(12,5))

plt.title("Top 10 Actors on Netflix")
plt.xlabel("Actor")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)

plt.savefig("images/top_10_actors.png")

plt.show()

# =====================================================
# EDA QUESTION 8
# Movie Duration Distribution
# =====================================================

movies = df[df["type"] == "Movie"].copy()

# Remove " min"
movies["duration"] = movies["duration"].str.replace(" min", "", regex=False)

# Convert to numeric
movies["duration"] = pd.to_numeric(movies["duration"], errors="coerce")

# Remove invalid values
movies = movies.dropna(subset=["duration"])

print("\nMovie Duration Statistics")
print(movies["duration"].describe())

movies["duration"].plot(kind="hist", bins=20, figsize=(10,5))

plt.title("Movie Duration Distribution")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Number of Movies")

plt.grid(True)

plt.savefig("images/movie_duration_distribution.png")

plt.show()

# =====================================================
# EDA QUESTION 9
# Content Added to Netflix by Year
# =====================================================

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

added_per_year = df["date_added"].dt.year.value_counts().sort_index()

print("\nContent Added by Year")
print(added_per_year)

added_per_year.plot(kind="line", figsize=(10,5))

plt.title("Content Added to Netflix by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles Added")

plt.grid(True)

plt.savefig("images/content_added_by_year.png")

plt.show()


# =====================================================
# EDA QUESTION 10
# Final Business Insights
# =====================================================

print("\n" + "="*50)
print("FINAL BUSINESS INSIGHTS")
print("="*50)

print(f"\nTotal Titles           : {len(df)}")

print(f"\nMovies                 : {type_counts['Movie']}")
print(f"TV Shows               : {type_counts['TV Show']}")

print(f"\nTop Country            : {country_counts.idxmax()}")
print(f"Titles                 : {country_counts.max()}")

print(f"\nMost Common Rating     : {rating_counts.idxmax()}")

print(f"\nTop Genre              : {genre_counts.idxmax()}")

print(f"\nTop Director           : {director_counts.idxmax()}")

print(f"\nTop Actor              : {actor_counts.idxmax()}")

print(f"\nHighest Release Year   : {year_counts.idxmax()}")
print(f"Titles Released        : {year_counts.max()}")

print("\nProject Completed Successfully!")
print("="*50)
