"""
Test data persistence
"""

import os

from payroll_calculator import constants
from payroll_calculator.data_manager.save_data import LocalFolderSaver

TARGET_FOLDER: str = constants.ROOT_DIR + "/tests/data_manager/output/"


def test_save_to_local_folder():
    """
    Test local folder saver
    :return:
    """

    records: list = ["name, salary", "RENE, 100", "MALCOM, 300", "CLAIRE, 400"]

    target_file = "payroll_test_1.csv"

    if os.path.exists(TARGET_FOLDER + target_file):
        os.remove(TARGET_FOLDER + target_file)

    data_saver = LocalFolderSaver()
    data_saver.save(records, TARGET_FOLDER + target_file)

    assert os.path.exists(TARGET_FOLDER + target_file) is True
