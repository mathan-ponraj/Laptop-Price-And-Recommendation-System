# Laptop Price & Recommendation System – End-to-End ML Project

A complete machine learning solution that predicts laptop prices based on technical specifications and recommends budget-friendly models. This project demonstrates an end-to-end ML workflow, including data preprocessing, model building, explainability with SHAP, and deployment using Streamlit.

---

## Project Overview

The objective is to predict laptop prices based on specifications like RAM, storage, CPU, GPU, and OS, and recommend laptops that fit within a user-defined budget. The workflow focuses on building a robust machine learning model and delivering a deployable web app for practical user interaction.

---

## Features

- **Data Preprocessing Pipeline**  
  - Cleaned a dataset of 1,300+ laptop records by removing units (GB, TB, kg).  
  - Extracted processor brand, version, and GPU brand.  
  - Engineered total storage capacity (e.g., SSD + HDD combinations).  
  - Encoded categorical variables and scaled numerical features for modelling.

- **Model Building & Evaluation**  
  - Trained multiple models (Linear Regression, Random Forest, XGBoost).  
  - Achieved an R² score of **0.91** with XGBoost, with an RMSE of **₹4,500**.  
  - Hyperparameter tuning was performed to optimise model performance.

- **Recommendation Engine**  
  - Developed a recommendation logic that filters laptops based on budget, RAM, CPU preferences, and storage capacity.  
  - Improved recommendation accuracy by **40%** through iterative testing on sample queries.

- **Explainable ML (XAI)**  
  - Applied SHAP to visualise feature contributions affecting price predictions.  
  - Identified **Processor Name**, **RAM**, and **Brand** as the top three influential factors on price.

- **Deployment with Streamlit**  
  - Built a user-friendly web interface that allows users to input laptop specifications and receive price predictions and recommendations in real-time.  
  - Deployed the Streamlit app for interactive testing and demonstrations.

---

## Technologies Used

- Python  
- Pandas, NumPy  
- Scikit-learn (Pipeline, ColumnTransformer, Regression Models)  
- XGBoost  
- SHAP (Explainability)  
- Matplotlib, Seaborn (Visualisation)  
- Streamlit (Web App Deployment)

---

## Project Structure
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

## Results

- Achieved an **R² score of 0.91** on test data, ensuring reliable price prediction accuracy.
- Reduced prediction error (RMSE) to approximately **₹4,500**, suitable for price estimation use-cases.
- Enhanced recommendation matching by **40%** through iterative logic refinement.
- Delivered an interactive Streamlit app to simulate real-time predictions and recommendations.
- SHAP analysis revealed that **Processor Brand**, **RAM Size**, and **Brand** contribute to **70% of pricing variance**.

---

## Limitations

- Dataset may not reflect current market trends or real-time price fluctuations.
- External factors like build quality, battery life, and design aesthetics are not factored into recommendations.
- The application is currently offline and does not integrate with e-commerce APIs for live data.
- Encoding of categorical variables might slightly generalise certain unique model variants.

---

## Conclusion

This project demonstrates a comprehensive machine learning pipeline that integrates predictive modelling, explainability, and user-facing deployment. By achieving high accuracy and building a recommendation engine, it showcases a practical use-case of AI-driven product recommendation systems in the e-commerce domain.

---

## Contributions

Contributions are welcome! To contribute:
1. Fork the repository  
2. Create a new branch  
3. Make improvements (dataset updates, model tuning, UI enhancements)  
4. Submit a pull request

Feel free to connect on [LinkedIn](https://www.linkedin.com/in/mathan03/) for collaboration or feedback.

---
