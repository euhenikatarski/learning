from kristina import Kristina

import pytest
from datetime import date


@pytest.fixture
def kristina():
    kristina = Kristina
    return kristina


def test_is_birthday_today(kristina):
    actual_date = date(2026, 12, 23)
    birthday_date = date(1998, 12, 23)
    assert actual_date.day == birthday_date.day and actual_date.month == birthday_date.month


def test_age(kristina):
    birth_date = date(1998,12,23)
    today = date(2025,11,23)
    years = today.year - birth_date.year
    if ((today.month, today.day) <
            (birth_date.month, birth_date.day)):
        years -= 1
    assert years == 26