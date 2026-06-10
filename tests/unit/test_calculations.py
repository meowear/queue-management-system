import pytest
from src.utils.calculations import calculate_wait_time

def test_calculate_wait_time_single_exit():
    # Position 10, 1 exit, 5 mins interaction time -> 50 mins
    assert calculate_wait_time(position=10, exits=1, interaction_time=5) == 50

def test_calculate_wait_time_multiple_exits():
    # Position 10, 2 exits, 5 mins interaction time -> 25 mins
    assert calculate_wait_time(position=10, exits=2, interaction_time=5) == 25

def test_calculate_wait_time_zero_position():
    assert calculate_wait_time(position=0, exits=1, interaction_time=5) == 0

def test_calculate_wait_time_invalid_exits():
    with pytest.raises(ValueError):
        calculate_wait_time(position=10, exits=0, interaction_time=5)
