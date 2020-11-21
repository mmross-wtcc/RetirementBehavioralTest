from pytest_bdd import scenarios, when, then
import pytest


from fullRetirementAge import *


CONVERTERS = {
    'birth_month': int,
}


scenarios('../features/retirement_month.feature', example_converters=CONVERTERS)


# When
@pytest.fixture
@when('the month "<birth_month>" is entered')
def input_month(birth_month):
    return birth_month


# Then
@then('the program raises a ValueError')
def get_retirement_age(input_month):
    with pytest.raises(ValueError):
        calculate_retirement_age(input_month)
