# tests/test_patient.py

from modules.Patient import Patient

# Test 1: Creating a patient
def test_create_patient():
    patient = Patient("P001", "Bob", "bob@email.com", 712345678, "1990-01-01")
    assert patient.patient_id == "P001"
    assert patient.name == "Bob"
    assert patient.email == "bob@email.com"

# Test 2: Patient name
def test_patient_name():
    patient = Patient("P002", "Alice", "alice@email.com", 712345678, "1995-05-05")
    assert patient.name == "Alice"

# Test 3: Patient email
def test_patient_email():
    patient = Patient("P003", "Charlie", "charlie@email.com", 712345678, "2000-01-01")
    assert "@" in patient.email  # email must have @

# Test 4: to_dict works
def test_patient_to_dict():
    patient = Patient("P001", "Bob", "bob@email.com", 712345678, "1990-01-01")
    result = patient.to_dict()
    assert result["name"] == "Bob"
    assert result["patient_id"] == "P001"