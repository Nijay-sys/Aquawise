def check_system_anomalies(ph, turbidity, hardness):
    
    reasons = []
    
    if ph < 0.0 or ph > 14.0:
        reasons.append(f"Invalid pH scale limit ({ph})")
    if turbidity < 0.0:
        reasons.append("Negative Turbidity reading")
    if hardness < 0.0:
        reasons.append("Negative Hardness reading")
  
    if turbidity > 15.0:
        reasons.append("Extreme Turbidity Spike (Sensor Blockage)")
    if hardness > 450.0:
        reasons.append("Critical Mineral Spike (Equipment Hazard)")
    if ph < 4.0 or ph > 10.0:
        reasons.append("Extreme pH Level (Corrosive Threat)")
        
    if reasons:
        return True, " & ".join(reasons)
    return False, "System Healthy"