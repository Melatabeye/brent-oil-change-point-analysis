import sys
import os
import pandas as pd

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.data_processing import clean_data


def test_clean_data_removes_missing_values():

    data = pd.DataFrame({
        "Date": ["2020-01-01", "2020-01-02"],
        "Price": [50, None]
    })

    cleaned = clean_data(data)

    assert cleaned.isnull().sum().sum() == 0