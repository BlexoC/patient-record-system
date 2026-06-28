# tests/test_ward.py

from modules.ward import Ward

# Test 1: Creating a ward
def test_create_ward():
    ward = Ward("W001", "ICU", "Dr Smith", 10)
    assert ward.ward_id == "W001"
    assert ward.ward_name == "ICU"
    assert ward.capacity == 10

# Test 2: Ward capacity
def test_ward_capacity():
    ward = Ward("W002", "General", "Dr Jones", 5)
    assert ward.capacity == 5
    assert ward.capacity > 0  # capacity must be positive

# Test 3: to_dict works
def test_ward_to_dict():
    ward = Ward("W001", "ICU", "Dr Smith", 10)
    result = ward.to_dict()
    assert result["ward_id"] == "W001"
    assert result["ward_name"] == "ICU"