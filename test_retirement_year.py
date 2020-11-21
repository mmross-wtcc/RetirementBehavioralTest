from pytest_bdd import scenarios, when, then
import pytest


from fullRetirementAge import *


CONVERTERS = {
    'birth_year': int,
}


scenarios('../features/retirement_year.feature', example_converters=CONVERTERS)


# When
@pytest.fixture
@when('the year "<birth_year>" is entered')
def input_year(birth_year):
    return birth_year


# Then
@then('the program raises a ValueError')
def get_retirement_age(input_year):
    with pytest.raises(ValueError):
        calculate_retirement_age(input_year)


