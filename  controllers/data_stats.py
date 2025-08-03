import pandas as pd
import numpy as np

def get_summary_statistics(df):
    """Return a DataFrame with mean, median, std for numeric columns."""
    summary = pd.DataFrame({
        "Mean": df.mean(numeric_only=True),
        "Median": df.median(numeric_only=True),
        "Std Dev": df.std(numeric_only=True)
    })
    return summary

def get_column_stats(df, column):
    """Return statistics for a specific column."""
    return {
        "Mean": np.mean(df[column]),
        "Median": np.median(df[column]),
        "Std Dev": np.std(df[column]),
        "Min": np.min(df[column]),
        "Max": np.max(df[column])
    }