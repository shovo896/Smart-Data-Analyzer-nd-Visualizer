import pandas as pd
import numpy as np

def calculate_mean(df, column):
    return np.mean(df[column])

def calculate_median(df, column):
    return np.median(df[column])

def calculate_std(df, column):
    return np.std(df[column])

def calculate_correlation(df, col1, col2):
    return df[col1].corr(df[col2])

def drop_missing(df):
    return df.dropna()

def fill_missing_with_mean(df):
    return df.fillna(df.mean(numeric_only=True))

def fill_missing_with_median(df):
    return df.fillna(df.median(numeric_only=True))

def filter_rows(df, column, operator, value):
    if operator == ">":
        return df[df[column] > value]
    elif operator == "<":
        return df[df[column] < value]
    elif operator == "=":
        return df[df[column] == value]
    else:
        return df

def sort_data(df, column, ascending=True):
    return df.sort_values(by=column, ascending=ascending)

def group_data(df, column):
    return df.groupby(column).size().reset_index(name="Count")