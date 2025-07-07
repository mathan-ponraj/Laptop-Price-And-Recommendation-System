# eda_laptop.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/data.csv")
print("✅ Data Loaded Successfully\n")

# Basic info
print("📌 Dataset Shape:", df.shape)
print("📌 Column Names:\n", df.columns.tolist())

print("\n🔍 Data Types & Nulls:")
print(df.info())

print("\n🧼 Missing Values:")
print(df.isnull().sum())

print("\n🎯 Statistical Summary:")
print(df.describe())

# --- Univariate Analysis ---
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True, bins=30)
plt.title("💰 Price Distribution")
plt.xlabel("Price (INR)")
plt.ylabel("Count")
plt.savefig("images/eda_price_distribution.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Brand', order=df['Brand'].value_counts().index)
plt.title("🏷️ Laptop Brand Count")
plt.xticks(rotation=45)
plt.savefig("images/eda_brand_count.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='RAM_GB', y='Price')
plt.title("🧠 Price vs RAM")
plt.savefig("images/eda_price_vs_ram.png")
plt.show()

# --- Bivariate Analysis ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='RAM_GB', y='Price', hue='Brand')
plt.title("🧠 RAM vs Price by Brand")
plt.savefig("images/eda_ram_price_brand.png")
plt.show()

# --- Correlation Heatmap ---
plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("📊 Correlation Heatmap")
plt.savefig("images/eda_correlation_heatmap.png")
plt.show()

# --- Rating Distribution ---
plt.figure(figsize=(8, 5))
sns.histplot(df['Rating'], kde=True, bins=10, color='orange')
plt.title("🌟 Rating Distribution")
plt.savefig("images/eda_rating_distribution.png")
plt.show()
