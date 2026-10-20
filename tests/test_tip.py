# Tests for tip.py
import pytest
from tip import calculate_tip


def test_basic_tip():
    tip, total, per_person = calculate_tip(100, 20, 1)
    assert tip == 20
    assert total == 120
    assert per_person == 120


def test_split_between_people():
    tip, total, per_person = calculate_tip(100, 20, 4)
    assert per_person == 30


def test_decimal_bill():
    tip, total, per_person = calculate_tip(47.83, 18, 3)
    assert tip == pytest.approx(8.6094)
    assert total == pytest.approx(56.4394)
    assert per_person == pytest.approx(18.8131, abs=0.0001)


def test_zero_tip():
    tip, total, per_person = calculate_tip(50, 0, 2)
    assert tip == 0
    assert per_person == 25


def test_zero_people_raises_error():
    with pytest.raises(ValueError):
        calculate_tip(50, 18, 0)