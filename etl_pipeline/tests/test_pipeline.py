import pytest
import sys
import os

# Add project root path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from etl.extract import extract

def test_extract():
    df = extract()

    assert not df.empty
    assert len(df) > 0