import pytest
from validator import validate_request

def test_valid_request():
    is_valid, error = validate_request({"question": "Test question"})
    assert is_valid is True
    assert error is None

def test_missing_question():
    is_valid, error = validate_request({})
    assert is_valid is False
    assert "question" in error.lower()

def test_question_too_long():
    long_text = "a" * 1001
    is_valid, error = validate_request({"question": long_text})
    assert is_valid is False
    assert "1000" in error

def test_additional_field():
    is_valid, error = validate_request({"question": "ok", "extra": "not allowed"})
    assert is_valid is False
    assert "additional properties" in error.lower()

def test_context_valid():
    is_valid, error = validate_request({
        "question": "test",
        "context": ["one", "two", "three"]
    })
    assert is_valid is True

def test_context_invalid_wrong_type():
    is_valid, error = validate_request({
        "question": "test",
        "context": [123, True]
    })
    assert is_valid is False
    assert "is not of type 'string'" in error