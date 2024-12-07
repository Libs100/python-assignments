import pytest
from seq import parse_file

def test_parse_simple_sequence():
    """Test a simple valid sequence of A, C, G, T."""
    sequence = "ACGTACGT"
    with open("test_simple.txt", "w") as f:
        f.write(sequence)
    result = parse_file("test_simple.txt")
    assert result == {'A': 2, 'C': 2, 'G': 2, 'T': 2, 'Unknown': 0, 'Total': 8}

def test_parse_with_mixed_characters():
    """Test a sequence with invalid characters."""
    sequence = "ACGTXYZ123"
    with open("test_mixed.txt", "w") as f:
        f.write(sequence)
    result = parse_file("test_mixed.txt")
    assert result == {'A': 1, 'C': 1, 'G': 1, 'T': 1, 'Unknown': 6, 'Total': 10}

def test_parse_empty_file():
    """Test an empty file."""
    with open("test_empty.txt", "w") as f:
        f.write("")
    result = parse_file("test_empty.txt")
    assert result == {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'Unknown': 0, 'Total': 0}

def test_parse_lowercase_sequence():
    """Test lowercase characters in a sequence."""
    sequence = "acgtacgt"
    with open("test_lowercase.txt", "w") as f:
        f.write(sequence)
    result = parse_file("test_lowercase.txt")
    assert result == {'A': 2, 'C': 2, 'G': 2, 'T': 2, 'Unknown': 0, 'Total': 8}

if __name__ == "__main__":
    try:
        pytest.main()
        print("\n✅ All tests passed successfully!")
    except Exception as e:
        print("\n❌ Some tests failed. Please check the errors.")
