import time
from enum import Enum
from time import struct_time


# Partial
class PeriodRelation(Enum):
    INSIDE = 0
    AFTER = 1
    BEFORE = 2


def is_inside(time_to_test: struct_time, interval_start: struct_time, interval_end: struct_time) -> bool:
    return interval_start <= time_to_test <= interval_end


def is_after(time_to_test: struct_time, interval_end: struct_time) -> bool:
    return time_to_test > interval_end


def is_before(time_to_test: struct_time, interval_start: struct_time) -> bool:
    return time_to_test < interval_start


def where_is(time_to_test: struct_time, interval_start: struct_time, interval_end: struct_time) -> PeriodRelation:

    if is_inside(time_to_test, interval_start, interval_end):
        return PeriodRelation.INSIDE
    elif is_after(time_to_test, interval_end):
        return PeriodRelation.AFTER
    elif is_before(time_to_test, interval_start):
        return PeriodRelation.BEFORE
