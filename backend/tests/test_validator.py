from backend.validation.output_validator import is_valid_output
from backend.validation.confidence_checker import is_confident

def test_is_valid_output():
    assert is_valid_output("This is fine.")
    assert not is_valid_output("   ")
    assert not is_valid_output("ERROR: something failed")

def test_is_confident():
    assert is_confident(0.9)
    assert not is_confident(0.5)
    assert is_confident(0.75)
