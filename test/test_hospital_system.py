# tests/test_hospital_system.py

import pytest
from services.Hospital_System import HospitalSystem
from modules.Patient import Patient
from modules.ward import Ward
from modules.administration import Administration

# ─────────────────────────────────────
# FIXTURES
# ─────────────────────────────────────

@pytest.fixture
def system():
    # fresh system for every test!
    s = HospitalSystem()
    return s

@pytest.fixture
def system_with_patient():
    s = HospitalSystem()
    s.patients.append(
        Patient("P001", "Bob", "bob@email.com", 712345678, "1990-01-01")
    )
    return s

@pytest.fixture
def system_with_ward():
    s = HospitalSystem()
    s.wards.append(
        Ward("W001", "ICU", "Dr Smith", 10)
    )
    return s

@pytest.fixture
def full_system():
    # system with everything set up!
    s = HospitalSystem()
    s.patients.append(
        Patient("P001", "Bob", "bob@email.com", 712345678, "1990-01-01")
    )
    s.patients.append(
        Patient("P002", "Alice", "alice@email.com", 712345679, "1995-05-05")
    )
    s.wards.append(
        Ward("W001", "ICU", "Dr Smith", 2)
    )
    s.wards.append(
        Ward("W002", "General", "Dr Jones", 5)
    )
    return s

# ─────────────────────────────────────
# PATIENT TESTS
# ─────────────────────────────────────

def test_find_patient(system_with_patient):
    result = system_with_patient.find_patient("P001")
    assert result is not None
    assert result.name == "Bob"

def test_find_patient_not_found(system):
    result = system.find_patient("P999")
    assert result is None  # should return None!

def test_patient_count(system_with_patient):
    assert len(system_with_patient.patients) == 1

def test_find_patient_case_insensitive(system_with_patient):
    # test uppercase and lowercase
    result = system_with_patient.find_patient("p001")
    assert result is not None
    assert result.name == "Bob"

# ─────────────────────────────────────
# WARD TESTS
# ─────────────────────────────────────

def test_find_ward(system_with_ward):
    result = system_with_ward.find_ward("W001")
    assert result is not None
    assert result.ward_name == "ICU"

def test_find_ward_not_found(system):
    result = system.find_ward("W999")
    assert result is None

def test_ward_count(system_with_ward):
    assert len(system_with_ward.wards) == 1

def test_ward_capacity(system_with_ward):
    ward = system_with_ward.find_ward("W001")
    assert ward.capacity == 10
    assert ward.capacity > 0

# ─────────────────────────────────────
# ADMISSION TESTS
# ─────────────────────────────────────

def test_admit_patient(full_system):
    # admit Bob to ICU
    full_system.administrations.append(
        Administration("P001", "W001")
    )
    enrolled = full_system.count_enrolled("W001")
    assert enrolled == 1

def test_already_administered(full_system):
    # admit Bob first time
    full_system.administrations.append(
        Administration("P001", "W001")
    )
    # check duplicate
    result = full_system.already_administered("P001", "W001")
    assert result == True  # already in ward!

def test_not_already_administered(full_system):
    result = full_system.already_administered("P001", "W001")
    assert result == False  # not admitted yet!

def test_ward_full(full_system):
    # ICU capacity is 2
    # admit both patients
    full_system.administrations.append(
        Administration("P001", "W001")
    )
    full_system.administrations.append(
        Administration("P002", "W001")
    )
    enrolled = full_system.count_enrolled("W001")
    ward = full_system.find_ward("W001")
    assert enrolled >= ward.capacity  # ward is full!

def test_discharge_patient(full_system):
    # admit first
    admin = Administration("P001", "W001")
    full_system.administrations.append(admin)
    assert full_system.count_enrolled("W001") == 1

    # discharge
    full_system.administrations.remove(admin)
    assert full_system.count_enrolled("W001") == 0

# ─────────────────────────────────────
# COUNT TESTS
# ─────────────────────────────────────

def test_count_enrolled_empty(system_with_ward):
    enrolled = system_with_ward.count_enrolled("W001")
    assert enrolled == 0  # nobody admitted yet!

def test_count_enrolled_after_admit(full_system):
    full_system.administrations.append(
        Administration("P001", "W001")
    )
    assert full_system.count_enrolled("W001") == 1