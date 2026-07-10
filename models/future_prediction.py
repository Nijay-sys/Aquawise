import pandas as pd

def forecast_sensor_trends(historical_df, lookback_entries=3, future_steps=3):
    
    if historical_df is None or len(historical_df) < 2:
        return None
     
    df_chrono = historical_df.iloc[::-1].reset_index(drop=True)
    
    predictions = {}
    target_features = ['ph', 'turbidity', 'hardness']
    
    for col in target_features:
        
        deltas = df_chrono[col].diff().dropna()
        
        avg_rate_of_change = deltas.tail(lookback_entries).mean()
        
        current_baseline = float(df_chrono[col].iloc[-1])
        
        future_projections = []
        for step in range(1, future_steps + 1):
            projected_val = current_baseline + (step * avg_rate_of_change)
            future_projections.append(round(projected_val, 2))
            
        predictions[col] = future_projections
        
    return predictions