import numpy as np

def analyze_dau(dau_list):
    # Convert input list to NumPy array for vectorized computation
    dau = np.array(dau_list, dtype=float)

    # Overall average across all days
    mean_dau = dau.mean()

    # Session logic: compare last 3 days with first 3 days
    first3_mean = dau[:3].mean()
    last3_mean = dau[-3:].mean()
    trend_delta = last3_mean - first3_mean

    # Positive delta means improving engagement trend
    is_uptrend = trend_delta > 0

    return {
        "mean_dau": mean_dau,
        "trend_delta": trend_delta,
        "is_uptrend": is_uptrend
    }

# Example usage
result = analyze_dau([120, 118, 125, 130, 128, 135, 140])
print(result)
