import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def run_ml_pipeline():
    db_path = 'd:/Web development Projects/project/data/gaming_health.db'
    
    print("Extracting sample dataset for ML Modeling (200,000 rows)...")
    conn = sqlite3.connect(db_path)
    
    # We select a subset of numeric and categorical features
    query = """
    SELECT age, gender, daily_gaming_hours, sleep_hours, caffeine_intake,
           anxiety_score, depression_score, social_interaction_score, 
           multiplayer_ratio, screen_time_total, addiction_level
    FROM gaming_data
    ORDER BY RANDOM()
    LIMIT 200000
    """
    df = pd.read_sql(query, conn)
    conn.close()
    
    # Preprocessing
    print("Preprocessing data...")
    # Handle categoricals 
    df = pd.get_dummies(df, columns=['gender'], drop_first=True)
    
    # Drop rows with NAs if any
    df = df.dropna()
    
    # Target and Features
    X = df.drop(columns=['addiction_level'])
    y = df['addiction_level']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Training XGBoost Regressor model...")
    model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluation
    predictions = model.predict(X_test_scaled)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    
    print(f"--- Model Evaluation ---")
    print(f"Root Mean Squared Error: {rmse:.4f}")
    print(f"R2 Score: {r2:.4f}")
    
    # Feature Importance Plot
    print("Generating Feature Importance visually...")
    importances = model.feature_importances_
    features = X.columns
    
    feat_imp = pd.DataFrame({'Feature': features, 'Importance': importances})
    feat_imp = feat_imp.sort_values(by='Importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=feat_imp, x='Importance', y='Feature', palette='magma')
    plt.title('Feature Importances for Predicting Addiction Level')
    plt.tight_layout()
    plt.savefig('d:/Web development Projects/project/reports/images/feature_importance.png', dpi=300)
    plt.close()
    
    print("ML Pipeline completed. Check reports/images/feature_importance.png.")

if __name__ == "__main__":
    run_ml_pipeline()
