from pytest_bdd import scenarios, given, when, then
import pytest


from fullRetirementAge import calculate_retirement_age


CONVERTERS = {
    'birth_year': int,
    'age_year': int,
    'age_month': int,
}


scenarios('../features/retirement_age.feature', example_converters=CONVERTERS)


# When
@pytest.fixture
@when('the year "<birth_year>" and month 5 are entered')
def input_birth_date(birth_year):
    return birth_year


# Then
@then('the program displays retirement age of "<age_year>" and "<age_month>"')
def get_retirement_age(age_year, age_month, input_birth_date):
    years, month = calculate_retirement_age(input_birth_date)
    retirement = (years, month)
    assert retirement == (age_year, age_month)



