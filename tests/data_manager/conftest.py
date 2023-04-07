import random
import pytest
from payroll_calculator import constants

NAMES = ["RUBEN", "CLAYTON", "JENNIE", "MARK", "PENELOPE", "LOUIS", "CAROL", "RICHARD", "EDUARD",
         "MARTIN", "JOLENA", "ANGIE", "DEREK", "NELSON", "BRAD"]

FILE_NAME: str = constants.ROOT_DIR + "/tests/data_manager//workdays_heavy.txt"
RECORDS: int = constants.TEST_RECORDS


@pytest.fixture(scope="session")
def gen_file():
    with open(FILE_NAME, "w+", encoding="utf-8") as file_pointer:
        for _ in range(RECORDS - 1):
            name = NAMES[random.randint(0, len(NAMES) - 1)]
            dummy_record = f"{name}=MO10:00-12:00,TU12:00-16:00,WE09:00-14:00,FR05:00-12:00,SA09:00-15:00\n"
            file_pointer.write(dummy_record)

        name: str = NAMES[random.randint(0, len(NAMES) - 1)]
        dummy_record = f"{name}=MO10:00-12:00,TU12:00-16:00,WE09:00-14:00,FR05:00-12:00,SA09:00-15:00"
        file_pointer.write(dummy_record)


@pytest.fixture(scope="session")
def gen_dummy_data(gen_file):
    def gen_function():
        return gen_file

    yield gen_function
