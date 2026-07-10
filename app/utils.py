import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aquawise.db')

def get_db_connection():
    """Establishes a connection to the self-contained SQLite database file."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def fetch_latest_data(limit=50):
    """Queries data from the SQLite file straight into a Pandas DataFrame."""
    if not os.path.exists(DB_PATH):
        return pd.DataFrame()
        
    conn = get_db_connection()
    query = f"SELECT * FROM water_telemetry ORDER BY timestamp DESC LIMIT {limit}"
    try:
        df = pd.read_sql(query, conn)
    except Exception:
        df = pd.DataFrame()
    conn.close()
    return df

def detect_anomaly(ph, turbidity, hardness):
    reasons = []
    
    if ph < 0 or ph > 14:
        reasons.append(f"Invalid pH scale ({ph})")
    if turbidity < 0:
        reasons.append("Negative Turbidity value")
    if hardness < 0:
        reasons.append("Negative Hardness value")
        
    if turbidity > 15.0:
        reasons.append("Extreme Turbidity Spike (Sensor Blockage)")
    if hardness > 450.0:
        reasons.append("Critical Mineral Spike (Equipment Hazard)")
    if ph < 4.0 or ph > 10.0:
        reasons.append("Extreme pH Level (Corrosive Environment)")
        
    if reasons:
        return True, " & ".join(reasons)
    return False, "Normal Telemetry"

def predict_future_trends(historical_df, steps=3):
    if len(historical_df) < 2:
        return None 
    df_chrono = historical_df.iloc[::-1].reset_index(drop=True)
    
    predictions = {}
    features = ['ph', 'turbidity', 'hardness']
    
    for col in features:
        deltas = df_chrono[col].diff().dropna()
        avg_delta = deltas.tail(3).mean() 
        
        last_val = float(df_chrono[col].iloc[-1])
        future_points = [round(last_val + (i * avg_delta), 2) for i in range(1, steps + 1)]
        predictions[col] = future_points
        
    return predictions