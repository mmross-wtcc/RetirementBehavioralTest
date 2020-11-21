def _validate_age_month(month):
    month = int(month)

    if month < 0 or month > 11:
        raise ValueError(f'Age month "{month}" must be between 0 and 11')

    return month


def _validate_age_year(year):
    year = int(year)

    if year < 65 or year > 67:
        raise ValueError(f'Age year "{year}" must be between 65 and 67')

    return year


def _validate_birth_month(month):
    month = int(month)

    if month < 1 or month > 12:
        raise ValueError(f'Birth month "{month}" must be between 1 and 12')

    return month


def _validate_birth_year(year):
    year = int(year)

    if year < 1900:
        raise ValueError(f'Birth year "{year}" must be no earlier than 1900')
    elif year >= 3000:
        raise ValueError(f'Birth year "{year}" must be earlier than 3000')

    return year

def calculate_retirement_age(year):
    """
    Calculates the expected retirement age/month
    Parameters:
        -year: birth year
    Returns:
        -retirement_age: age (in years) a person will retire
        -retirement_month: the months a person will retire
    """
    birth_year = _validate_birth_year(year)

    if year <= 1937:
        retirement_age = 65
        retirement_month = 0
    elif year == 1938:
        retirement_age = 65
        retirement_month = 2
    elif year == 1939:
        retirement_age = 65
        retirement_month = 4
    elif year == 1940:
        retirement_age = 65
        retirement_month = 6
    elif year == 1941:
        retirement_age = 65
        retirement_month = 8
    elif year == 1942:
        retirement_age = 65
        retirement_month = 10
    elif 1943 <= year <= 1954:
        retirement_age = 66
        retirement_month = 0
    elif year == 1955:
        retirement_age = 66
        retirement_month = 2
    elif year == 1956:
        retirement_age = 66
        retirement_month = 4
    elif year == 1957:
        retirement_age = 66
        retirement_month = 6
    elif year == 1958:
        retirement_age = 66
        retirement_month = 8
    elif year == 1959:
        retirement_age = 66
        retirement_month = 10
    else:
        retirement_age = 67
        retirement_month = 0

    return retirement_age, retirement_month


def calculate_retirement_date(birth_year, birth_month, ret_age, ret_month):
    """
    Calculates the expected retirement date (month/year)
    Parameters:
        -birth_year: year of birth
        -birth_month: month of birth
        -ret_age: expected retirement age in years
        -ret_month: expected months to retire
    Returns:
        -estimated_month_str: month expected to retire in
        -estimated_year: year expected to retire in
    """
    birth_year = _validate_birth_year(birth_year)
    birth_month = _validate_birth_month(birth_month)
    ret_age = _validate_age_year(ret_age)
    ret_month = _validate_age_month(ret_month)
    # List of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Calculate estimated month/year
    estimated_year = birth_year + ret_age
    estimated_month = birth_month + ret_month

    # Change months to a year if necessary
    if estimated_month > 12:
        estimated_year += 1
        estimated_month -= 12

    # Change month int to a month string based on the month
    estimated_month_str = months[estimated_month-1]
    return estimated_month_str, estimated_year


