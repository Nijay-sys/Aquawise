import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

def clean_water_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_path = os.path.join(current_dir, '..', 'Dataset', 'water_potability.csv')
    cleaned_data_path = os.path.join(current_dir, '..', 'Dataset', 'cleaned_water_data.csv')

    if not os.path.exists(raw_data_path):
        print(f"❌ Error: Cannot find dataset at: {os.path.abspath(raw_data_path)}")
        return None

    df = pd.read_csv(raw_data_path)
    df.columns = df.columns.str.strip()
    
    required_cols = ['ph', 'Turbidity', 'Hardness', 'Potability']
    df = df[required_cols]
    
    # Clean using grouped targets
    features_to_clean = ['ph', 'Turbidity', 'Hardness']
    for col in features_to_clean:
        df[col] = df.groupby('Potability')[col].transform(lambda x: x.fillna(x.median()))

    # Moderate clipping limits to let extreme contaminated metrics stand out clearly
    for col in features_to_clean:
        Q1 = df[col].quantile(0.10)
        Q3 = df[col].quantile(0.90)
        df[col] = np.clip(df[col], Q1, Q3)

    df.to_csv(cleaned_data_path, index=False)
    return cleaned_data_path

def train_potability_model(cleaned_data_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_output_path = os.path.join(current_dir, 'water_model.pkl')
    scaler_output_path = os.path.join(current_dir, 'scaler.pkl')

    df = pd.read_csv(cleaned_data_path)

    X = df[['ph', 'Turbidity', 'Hardness']]
    y = df['Potability']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Standardize scaling configurations safely
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    print("🏋️ Training Balanced Random Forest Classifier...")
    # class_weight="balanced" forces the ML engine to respect contaminated configurations accurately
    model = RandomForestClassifier(n_estimators=150, max_depth=12, class_weight="balanced", random_state=42)
    model.fit(X_train_scaled, y_train)

    # Save matching setup components
    joblib.dump(model, model_output_path)
    joblib.dump(scaler, scaler_output_path)
    print("🎯 Model and configuration Scaler successfully recalibrated and saved!")

if __name__ == "__main__":
    cleaned_path = clean_water_data()
    if cleaned_path:
        train_potability_model(cleaned_path)