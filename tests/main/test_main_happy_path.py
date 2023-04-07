from payroll_calculator import constants
from payroll_calculator import main

DATA_FOLDER_PATH = constants.ROOT_DIR + "/tests/data_manager/"


def test_main_full_process_process():

    main.process_payroll(DATA_FOLDER_PATH + "workdays_heavy.txt",
                         "payroll_main.txt")
