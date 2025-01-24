# **Laptop Price and Recommendation System**

This project predicts laptop prices based on key specifications and provides recommendations for users. It utilizes data preprocessing, machine learning models, and feature engineering to deliver accurate price predictions. The recommendation system is designed to help users identify budget-friendly laptops based on their preferences.

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Dataset](#dataset)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Results](#results)
8. [Limitations](#limitations)
9. [Contributions](#contributions)

---

## **Introduction**
Laptop prices vary based on technical specifications such as processor type, RAM, storage, and GPU. This project aims to:
- Predict laptop prices based on their specifications.
- Recommend laptops within a user-defined budget.

The project leverages machine learning models to predict prices and offers insights into the relationship between hardware specifications and costs.

---

## **Features**
- Import and utilize essential Python libraries.
- Data cleaning and preprocessing for better model performance.
- Implementation of machine learning models for price prediction.
- Recommendation system for budget-friendly laptops based on user preferences.
- Model evaluation and visualization of results.

---

## **Technologies Used**
1. **Python**: Core programming language.
2. **Pandas, NumPy**: For data manipulation and analysis.
3. **Matplotlib, Seaborn**: For data visualization.
4. **Scikit-learn**: For machine learning models and evaluation.
5. **Google Colaboratory**: For executing the notebook seamlessly.

---

## **Dataset**
The dataset contains various laptop specifications and corresponding prices. Key features include:
- `Processor_name,processor_gen`: Type of processor (e.g., Intel Core i5, AMD Ryzen 5).
- `RAM`: Size of RAM in GB.
- `Storage`: Type and size of storage (e.g., 256GB SSD, 1TB HDD).
- `Brand`: Brand name of the laptop.

The dataset is included:
- Dataset files into a `data/` folder:
  - `laptop_price_recommendation_cleaned_dataset.csv`: Original dataset.
  - `input_features.csv,output_features.csv`: Cleaned dataset after preprocessing.

---

## **Setup and Installation**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/laptop-price-recommendation.git
   cd laptop-price-recommendation
  

2. Install the required dependencies:

   ```
    pip install -r requirements.txt
   

3. Open the project in Google Colaboratory or Jupyter Notebook:
 ```
   jupyter notebook notebooks/laptop_price_prediction.ipynb

 ```
---
## Usage

1. Open the Jupyter Notebook /Google colob file located in the `notebooks/` directory.
2. Follow the steps outlined in the notebook to:
   - Preprocess the dataset.
   - Train and evaluate machine learning models.
   - Use the recommendation system to find budget-friendly laptops.
3. Modify hyperparameters or dataset values within the notebook to explore different scenarios.

---
## **Results**
- The trained machine learning models successfully predicted laptop prices with high accuracy.
- The following algorithms were used, and their evaluation metrics are as follows:
  - Linear Regression: R² = 0.85
- The recommendation system provided accurate suggestions for budget-friendly laptops based on user preferences.

## **Limitations**
- The dataset may not include the latest laptop models, which could affect the relevance of the predictions.
- The recommendation system is primarily based on budget and does not incorporate additional user preferences such as operating system, battery life, or design,etc,.
- Model performance is dependent on the quality and diversity of the dataset. A more diverse dataset may yield better results.
- The system currently works offline and lacks integration with live e-commerce data.
- Some times the encoding and decoding encounders miss matching data between original and predicted.


---
## **Contributions**

Contributions are welcome! If you'd like to improve the project, feel free to collaborate. You can reach out to me via [LinkedIn](https://www.linkedin.com/in/mathan03/) to discuss or propose improvements.


