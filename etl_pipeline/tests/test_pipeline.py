import pytest
import numpy as np
import sys
import os

# pytest tests/test_pipeline.py (to run)


# Add project root path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Testing extract
from etl.extract import extract

# Check that there is data
def test_extract():
    data = extract()
    assert data is not None

# Testing transform
from etl.transform import transform

def test_transform_null():
    data = extract()
    df = transform(data)
    assert np.where(df["timestamp"].isnull())

def test_transform_dtype():
    data = extract()
    df = transform(data)
    assert df["id"].dtype == int