import time
from payroll_calculator.utils import time_interval_algebra as tia


def test_is_before_true():
    time_to_test = time.strptime("10:00", "%H:%M")
    interval_start = time.strptime("10:30", "%H:%M")

    assert tia.is_before(time_to_test, interval_start) is True


def test_is_before_false():
    time_to_test = time.strptime("13:00", "%H:%M")
    interval_start = time.strptime("10:30", "%H:%M")

    assert tia.is_before(time_to_test, interval_start) is False


def test_is_inside_true():
    time_to_test = time.strptime("13:00", "%H:%M")
    interval_start = time.strptime("10:30", "%H:%M")
    interval_end = time.strptime("15:45", "%H:%M")

    assert tia.is_inside(time_to_test, interval_start, interval_end) is True


def test_is_inside_false_before():
    time_to_test = time.strptime("9:00", "%H:%M")
    interval_start = time.strptime("10:30", "%H:%M")
    interval_end = time.strptime("15:45", "%H:%M")

    assert tia.is_inside(time_to_test, interval_start, interval_end) is False


def test_is_inside_false_after():
    time_to_test = time.strptime("17:00", "%H:%M")
    interval_start = time.strptime("10:30", "%H:%M")
    interval_end = time.strptime("15:45", "%H:%M")

    assert tia.is_inside(time_to_test, interval_start, interval_end) is False


def test_is_after_true():
    time_to_test = time.strptime("12:00", "%H:%M")
    interval_end = time.strptime("10:30", "%H:%M")

    assert tia.is_after(time_to_test, interval_end) is True


def test_is_after_false():
    time_to_test = time.strptime("09:00", "%H:%M")
    interval_end = time.strptime("10:30", "%H:%M")

    assert tia.is_after(time_to_test, interval_end) is False


def test_where_is_before():
    time_to_test = time.strptime("09:00", "%H:%M")
    interval_start = time.strptime("10:30", "%H:%M")
    interval_end = time.strptime("15:45", "%H:%M")

    assert tia.where_is(time_to_test, interval_start, interval_end) == tia.PeriodRelation.BEFORE


def test_where_is_inside():
    time_to_test = time.strptime("11:00", "%H:%M")
    interval_start = time.strptime("10:30", "%H:%M")
    interval_end = time.strptime("15:45", "%H:%M")

    assert tia.where_is(time_to_test, interval_start, interval_end) == tia.PeriodRelation.INSIDE


def test_where_is_after():
    time_to_test = time.strptime("17:00", "%H:%M")
    interval_start = time.strptime("10:30", "%H:%M")
    interval_end = time.strptime("15:45", "%H:%M")

    assert tia.where_is(time_to_test, interval_start, interval_end) == tia.PeriodRelation.AFTER
