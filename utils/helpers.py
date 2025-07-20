# Utility helper functions
# Updated import
import numpy as np
# Updated import
import pandas as pd

def normalize_data(data):
    """Normalize data to [0, 1] range"""
    return (data - data.min()) / (data.max() - data.min())

def calculate_accuracy(y_true, y_pred):
    """Calculate accuracy score"""
    return np.mean(y_true == y_pred)



# TODO: Review implementation

# Last updated: 2025-12-11




# Updated: 2025-12-11
