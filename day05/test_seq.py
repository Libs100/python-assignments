import pytest
from seq import calculate_statistics

def test_calculate_statistics_with_good_data():
    sequence = "AAGGTTCC"
    result = calculate_statistics(sequence)
    expected = {
        "A": (2, 25.0),
        "C": (2, 25.0),
        "G": (2, 25.0),
        "T": (2, 25.0),
        "Unknown": (0, 0.0),
        "Total": 8
    }
    assert result == expected

def test_calculate_statistics_with_mixed_data():
    sequence = "AAGXCTGGX"
    result = calculate_statistics(sequence)
    expected = {
        "A": (2, 20.0),
        "C": (1, 10.0),
        "G": (3, 30.0),
        "T": (1, 10.0),
        "Unknown": (2, 20.0),
        "Total": 10
    }
    assert result == expected

def test_calculate_statistics_empty_sequence():
    sequence = ""
    result = calculate_statistics(sequence)
    expected = {
        "A": (0, 0.0),
        "C": (0, 0.0),
        "G": (0, 0.0),
        "T": (0, 0.0),
        "Unknown": (0, 0.0),
        "Total": 0
    }
    assert result == expected
