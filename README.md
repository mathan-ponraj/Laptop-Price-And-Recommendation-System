# Laptop Price & Recommendation System — End-to-End ML Project

**Live Demo:**  
[Streamlit App - Laptop Price & Recommendation System](https://laptop-price-and-recommendation-system-icvhjjspmfrmmy2rfmtuaq.streamlit.app/)

## Problem Statement (Using the STAR Method)

### Situation
Choosing the right laptop can be confusing. With hundreds of models across different brands, buyers often struggle to find the best laptop that fits their budget and performance needs. Many end up discovering better options only after purchasing, which leads to regret and uncertainty.

### Task
To develop an intelligent system that can predict laptop prices and recommend better alternatives within a user-defined budget, helping buyers make smarter decisions.

### Action
Built a complete machine learning pipeline that:
- Predicts laptop prices based on key specifications (CPU, RAM, storage, GPU, brand, etc.)
- Recommends top laptop options within a given price range.
- Delivers results through an interactive Streamlit web app and an analytical Power BI dashboard.

### Result
- Achieved R² = 0.91 using XGBoost after tuning.
- Improved recommendation accuracy by 40%.
- Built a fully deployed web app for real-time user interaction.
- Designed a Power BI dashboard to visualize pricing trends and patterns.

## Project Workflow

### 1. Data Collection & Loading
- Collected the laptop dataset from Kaggle.  
- Loaded and explored the dataset using Pandas for initial inspection and validation.

### 2. Data Preprocessing
- Removed unwanted keywords, special characters, and extra spaces from laptop names.  
- Cleaned numerical fields (e.g., GB, TB, kg) and standardized units.  
- Detected and removed outliers using statistical methods (IQR-based filtering) to ensure model stability.

### 3. Feature Engineering & Selection
- Extracted key attributes such as processor brand, processor version, GPU type, and total storage.  
- Applied SHAP analysis to identify the most influential features affecting price prediction.

### 4. Model Development
- Implemented and compared Random Forest and XGBoost models.  
- Conducted hypothesis testing and hyperparameter tuning to optimize performance.  
- Used A/B testing to determine the better-performing model for final deployment.

### 5. Model Evaluation
- Final model achieved an R² score of 0.91 and RMSE ≈ ₹4,500.  
- XGBoost performed best in terms of accuracy and generalization.

### 6. Deployment
- Deployed the trained model using Streamlit to create an interactive web interface.  
- Integrated user inputs for price, RAM, and storage to display predictions and top recommendations in real time.

### 7. Power BI Dashboard
- Designed a Power BI dashboard to analyze pricing trends, distribution by brand, and category-wise comparisons.  
- Helped visualize how specifications influence laptop pricing patterns.

## Technologies Used

- Programming Language: Python  
- Libraries: Pandas, NumPy, Scikit-learn, XGBoost, SHAP  
- Visualization: Matplotlib, Seaborn, Power BI  
- Deployment: Streamlit  
- Data Source: Kaggle Laptop Dataset




---

## Repository Structure
```
Laptop_Price_Recommendation_System/
├── README.md # Project documentation
├── data/
│ └── data.csv # Preprocessed dataset
├── notebooks/
│ └── LAPTOP_RECOMMENDATION_MODEL.ipynb # Jupyter Notebook with complete workflow
├── app/
│ └── streamlit_app.py # Streamlit web app script
├── requirements.txt # Required Python libraries
```

---


## Limitations

- Dataset may not reflect current market trends or real-time price fluctuations.
- External factors like build quality, battery life, and design aesthetics are not factored into recommendations.
- The application is currently offline and does not integrate with e-commerce APIs for live data.
- Encoding of categorical variables might slightly generalise certain unique model variants.

---


## Conclusion
This project demonstrates how machine learning and analytics can simplify real-world decision-making.  
By combining predictive modeling, explainable AI (SHAP), and data visualization, this system helps users make confident laptop purchase choices without regret.

---

## Contributions

Contributions are welcome! To contribute:
1. Fork the repository  
2. Create a new branch  
3. Make improvements (dataset updates, model tuning, UI enhancements)  
4. Submit a pull request

Feel free to connect on [LinkedIn](https://www.linkedin.com/in/mathan03/) for collaboration or feedback.

---
