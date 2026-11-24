# Student: Thet Htoo Naing
# Student ID: 6705140009

import pytest
from validators import validate_email, validate_age

def test_email_without_at_rejected():
    with pytest.raises(ValueError):
        validate_email("notanemail.com")

def test_email_without_domain_rejected():
    with pytest.raises(ValueError):
        validate_email("user@")

def test_negative_age_rejected():
    with pytest.raises(ValueError):
        validate_age(-5)

def test_age_as_string_rejected():
    with pytest.raises(TypeError):
        validate_age("twenty")


@pytest.mark.parametrize("age", [True, False])
def test_boolean_age_rejected(age):
    with pytest.raises(TypeError):
        validate_age(age)


def test_email_with_trailing_newline_rejected():
    with pytest.raises(ValueError):
        validate_email("student@siam.ac.th\n")
