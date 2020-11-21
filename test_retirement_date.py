from pytest_bdd import scenarios, when, then
import pytest

from fullRetirementAge import *


CONVERTERS = {
    'birth_month': int,
    'est_year': int,
    'est_month': str,
}


scenarios('../features/retirement_date.feature', example_converters=CONVERTERS)


# When
@pytest.fixture
@when('the year 1942 and the month "<birth_month>" is entered')
def input_birth_date(birth_month):
    return birth_month


# Then
@then('the program displays estimated retirement year "<est_year>" and estimated retirement month "<est_month>"')
def get_retirement_date(est_year, est_month, input_birth_date):
    assert calculate_retirement_date(1942, input_birth_date, 65, 10) == (est_month, est_year)



