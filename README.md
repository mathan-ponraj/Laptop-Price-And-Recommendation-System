# Laptop Price & Recommendation System

A complete end-to-end machine learning solution that predicts laptop prices based on technical specifications and recommends budget-friendly models. The system features a full ML pipeline, a real-world deployment-ready web app (via Streamlit), and visual insights powered by a clean recommendation engine.

---

## Table of Contents
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

## Introduction

Laptop pricing varies greatly based on factors like CPU, RAM, storage, GPU and brand. This system:
- Predicts laptop prices with high accuracy using machine learning.
- Recommends the best laptops under a given budget based on key user preferences.

It includes data cleaning, feature engineering, model training, explainability (with SHAP), and a deployed Streamlit web app for user interaction.

---

## Features

- End-to-end preprocessing pipeline:
  - Removed units (e.g. ‘GB’, ‘kg’) for clean numerical inputs  
  - Extracted CPU brand, core name, and GPU brand  
  - Engineered total memory (e.g. 128GB SSD + 1TB HDD → 1152GB)  
  - Applied label and one-hot encoding for model-ready inputs  
- Trained multiple ML models (Linear Regression, Random Forest, XGBoost)  
- R² score up to 0.91 with XGBoost  
- Recommendation engine based on price range, RAM, and CPU filters  
- SHAP visualisation to explain model predictions  
- Deployed Streamlit app for real-time price prediction and recommendations

---

## Technologies Used

- Languages & Libraries: Python, Pandas, NumPy, Scikit-learn, XGBoost, SHAP  
- Visualisation: Matplotlib, Seaborn  
- Interface & Deployment: Streamlit (Cloud), Jupyter Notebook, VS Code

---

## Dataset

The original dataset contained multiple specifications for each laptop. After analysis and feature selection based on model performance and interpretability, the following key features were retained:

- `Name`: Model name of the laptop  
- `Brand`: Laptop manufacturer  
- `RAM`: Amount of RAM in GB  
- `Storage`: Total internal storage in GB  
- `Storage_Type`: Whether the storage is HDD, SSD, or hybrid  
- `OS`: Operating system installed  
- `Processor_Name`: Combined field of processor brand, version, and generation

### Preprocessing Steps:
- Removed unnecessary columns based on low feature importance (identified through model evaluation)
- Combined processor details (`Processor_Brand`, `Version`, `Generation`) into a single column `Processor_Name`
- Handled missing values and unit conversion (e.g. 'GB', 'TB')
- Label and One-Hot Encoding applied for categorical variables as needed
- Normalised numerical features like `RAM` and `Storage`
Data Files:
- `data.csv ` Preprocessed and model-ready data  

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/laptop-price-recommendation.git
   cd laptop-price-recommendation
`

 **Data Files**:
- `data.csv`: Original raw data.


---

##  **Setup and Installation**

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/laptop-price-recommendation.git
   cd laptop-price-recommendation
   ```

2.Install dependencies:
  ```bash
pip install -r requirements.txt
```
3. Run the notebook:
   ```bash
   jupyter notebook notebooks/LAPTOP_RECOMMENDATION_MODEL.ipynb
   ```
   Or open the `.ipynb` file directly in Google Colab or VS Code with the Jupyter extension.

---

## Usage

### Data Preprocessing
- Handle missing values  
- Encode categorical features  
- Normalise or scale numerical columns  

### Train the Model
- Choose an algorithm (default: **XGBoost**)  
- Evaluate performance using metrics like **R² score** and **RMSE**

### Make Predictions
- Input laptop specifications  
- Predict the selling price using the trained model  

### Get Recommendations
- Enter your budget, brand, and required specs  
- Receive filtered and sorted laptop recommendations based on predicted price and specs  

---

## Results

| Model     | R² Score | RMSE (approx) |
|-----------|----------|---------------|
| XGBoost   | 0.91     | ₹4,500         |

- The model accurately predicts laptop prices with an **R² score of 0.91**
- The recommendation engine suggests laptops that best match user requirements within budget constraints  

---

## Limitations

- The dataset may not reflect the **latest laptop models** or price fluctuations  
- Recommendations are based on selected specifications and don’t account for factors like **battery life**, **screen quality**, or **design**  
- The app currently works **offline** and doesn’t integrate with real-time retailer APIs  
- Some encoded feature values might differ slightly from the original category labels  

---

## Contributions

Contributions are welcome! If you’d like to help improve the dataset, model, or user interface:

- Fork the repository  
- Make your changes  
- Submit a pull request  

Feel free to connect on [LinkedIn](https://www.linkedin.com/in/mathan03/) for collaboration or feedback.
