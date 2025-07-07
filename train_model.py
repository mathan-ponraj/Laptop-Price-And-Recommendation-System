import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import numpy as np

# Load dataset
data = pd.read_csv("data/data.csv")
print("✅ Dataset loaded")

# Target
y = data['Rating']

# Features (including both categorical & numeric)
X = data[['Brand', 'RAM_GB', 'Storage', 'Price', 'Processor_name', 'OS']]

# Drop missing values
X = X.dropna()
y = y.loc[X.index]  # Keep y aligned

# Winsorize (cap) 'Price' outliers
q1 = X['Price'].quantile(0.01)
q99 = X['Price'].quantile(0.99)
X['Price'] = X['Price'].clip(lower=q1, upper=q99)

# Apply log transformation to the target variable to stabilise outliers
y = np.log1p(y)

# Identify column types
categorical_cols = X.select_dtypes(include='object').columns.tolist()
numerical_cols = X.select_dtypes(include='number').columns.tolist()

# Preprocessing for numeric and categorical columns
numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# XGBoost pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('xgb', XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)
print("✅ Model trained")

# Predict and inverse log transform
y_pred_log = model.predict(X_test)
y_pred = np.expm1(y_pred_log)  # convert back to original scale
y_test_original = np.expm1(y_test)  # actual target in original scale

# Evaluation
rmse = mean_squared_error(y_test_original, y_pred)
r2 = r2_score(y_test_original, y_pred)
print(f"📉 RMSE: {rmse:.2f}")
print(f"📈 R² Score: {r2:.2f}")
print("accuracyscore:", model.score(X_test, y_test))
# Save model
joblib.dump(model, 'model/model.pkl')
print("💾 Model pipeline saved at model/model.pkl")
