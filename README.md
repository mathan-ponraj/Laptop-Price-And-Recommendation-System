# 💻 **Laptop Price & Recommendation System**

This project accurately predicts laptop prices based on technical specifications and helps users discover budget-friendly laptops. It features preprocessing techniques, machine learning models, and a recommendation engine, all built using a real-world dataset.

---

## 📌 **Table of Contents**
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

## 📖 **Introduction**

Laptop prices depend heavily on specifications like processor brand, core type, RAM, storage, GPU, and weight. This system:
- Predicts laptop prices using machine learning.
- Recommends laptops within a user's preferred budget and features.

It leverages a trained **Linear Regression** model and feature engineering to provide meaningful insights.

---

## ✨ **Features**

- ✅ Preprocessing pipeline including:
  - Cleaning data (unit removal like 'GB', 'kg').
  - Extracting `Cpu_Brand`, `Core_Name`, and `Gpu_Brand`.
  - Feature engineering for memory capacity.
  - Encoding (Label & One-Hot).
- 🧠 Linear Regression model for price prediction (R² = 0.85).
- 💡 Recommendation engine based on price, RAM, and CPU filters.
- 🔁 Decoding function for encoded results back to human-readable values.

---

## 🛠 **Technologies Used**
- **Python**: Core language.
- **Pandas & NumPy**: Data processing.
- **Matplotlib & Seaborn**: Visualizations.
- **Scikit-learn**: Machine learning pipeline.
- **Google Colab / Jupyter Notebook**: Execution environment.

---

## 📊 **Dataset**

The dataset includes specs and prices of laptops, with features like:
- `Company`, `TypeName`, `RAM`, `Weight`
- `Cpu`, `Gpu`, `Memory`
- `OpSys`, `Price_euros`

### 🔧 After preprocessing:
- **Price** converted to INR (multiplied by 90.97).
- **Memory** extracted and summed (e.g., `128GB SSD + 1TB HDD` = `1152GB`).
- **CPU** split into `Cpu_Brand` and `Core_Name`.
- **Label Encoding** used for:
  - `Cpu_Brand`, `Core_Name`
- **One-Hot Encoding** used for:
  - `Company`, `TypeName`, `OpSys`, `Gpu_Brand`

📁 **Data Files**:
- `laptop_price.csv`: Original raw data.
- `input_features.csv`, `output_features.csv`: Cleaned and processed features.

---

## ⚙️ **Setup and Installation**

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/laptop-price-recommendation.git
   cd laptop-price-recommendation
   ```

2.Install dependencies:
  ```bash
pip install -r requirements.txt
```
3.Run the notebook:
```bash
jupyter notebook notebooks/LAPTOP_RECOMMENDATION_MODEL.ipynb
```
Or use Google Colab to open the .ipynb file directly.

## **Usage**

### **Data Preprocessing**
- Handle null values  
- Encode categorical features  
- Normalize or scale numeric columns  

### **Train the Model**
- Choose algorithm (default: **Linear Regression**)  
- Evaluate using metrics like **R²**

### **Make Predictions**
- Input laptop features  
- Predict price using the trained model  

### **Get Recommendations**
- Enter your budget, brand preference, and specs  
- Receive filtered and sorted laptop suggestions  

---

## **Results**

| **Model**            | **R² Score** | **RMSE** |
|----------------------|--------------|----------|
| Linear Regression    | 0.85         | ~7000    |
| Random Forest        | 0.89         | ~5000    |
| Gradient Boosting    | 0.91         | ~4500    |

- 📌 The model accurately predicts prices with an **R² of up to 0.91**.
- 🔎 The recommendation engine returns **best-matched laptops under the specified budget**.

---

## **Limitations**
- 📆 Dataset may not reflect the **latest laptop models**.  
- ⚙️ Recommendations are **spec-limited** (budget, RAM, brand) and don’t include deeper metrics like **battery life or design**.  
- 🔌 **Offline only**: Does not fetch live data from online retailers.  
- ⚠️ Possible **mismatch between encoded model values and original categories**.  

---

## **Contributions**

Contributions are highly appreciated! If you have ideas to improve the dataset, models, or UI, feel free to:

- ✅ Fork the repo  
- ✅ Make changes  
- ✅ Create a pull request  

Or reach out on [LinkedIn](https://www.linkedin.com/in/mathan03/) to connect and collaborate!

