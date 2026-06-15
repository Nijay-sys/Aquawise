import streamlit as st
import pandas as pd
import joblib
import os

from utils import fetch_latest_data, detect_anomaly

st.set_page_config(page_title="AquaWise Analytics Node", layout="wide")

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '..', 'models', 'water_model.pkl')
scaler_path = os.path.join(current_dir, '..', 'models', 'scaler.pkl')

try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
except Exception as e:
    st.warning("ML Model or Scaler not loaded yet.")
    model, scaler = None, None

st.title("📊 Real-Time Analytics Dashboard")

df_metrics = fetch_latest_data(limit=50)

if not df_metrics.empty:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("💡 Latest Live Telemetry")
        latest_entry = df_metrics.iloc[0]
        
        st.metric(label="pH Level", value=f"{latest_entry['ph']:.2f}")
        st.metric(label="Turbidity (NTU)", value=f"{latest_entry['turbidity']:.2f}")
        st.metric(label="Hardness (mg/L)", value=f"{latest_entry['hardness']:.2f}")
        
        if model and scaler:
            input_features = pd.DataFrame([[latest_entry['ph'], latest_entry['turbidity'], latest_entry['hardness']]], 
                                          columns=['ph', 'Turbidity', 'Hardness'])
            scaled_features = scaler.transform(input_features)
            prediction = model.predict(scaled_features)[0]

            if not latest_entry.empty:
                latest_row = latest_entry.iloc[0]

                is_anomalous, anomaly_reason = detect_anomaly(
                    float(input_features['ph'].iloc[0]), 
                    float(input_features['Turbidity'].iloc[0]), 
                    float(input_features['Hardness'].iloc[0])
           )
            
            if is_anomalous:
                st.error(f"🚨 **ANOMALY ALERT:** {anomaly_reason}")
            else:
                st.success("✅ **Sensor Health:** System Stable & Calibrated")

    with col2:
        st.subheader("📈 Sensor Fluctuations Over Time")
        st.line_chart(df_metrics.set_index('timestamp')[['ph', 'turbidity']])
        
    st.subheader("📋 Logged Data Registry (MySQL Mirror)")
    st.dataframe(df_metrics, use_container_width=True)
else:
    st.info("Awaiting telemetric stream transmission to MySQL framework...")