import sys
import os
import logging
from payroll_calculator.data_manager.load_data import (DataLoaderFactory,
                                                       LocalFolderLoader)
from payroll_calculator.payroll.payroll_calculator import EmployeeSalary
from payroll_calculator.data_manager.transformations import ParseWorkedDayData
from payroll_calculator.data_manager.save_data import DataSaverFactory
from payroll_calculator.data_manager.data_manager_types import DataFileSource

HELP_LINE = "python main.py <input_file_name> <output_file_name>"


def load_data(file_path: str) -> list:
    data_loader: LocalFolderLoader = DataLoaderFactory(
        DataFileSource.LOCAL_FOLDER
    ).get_loader()

    try:
        worked_days_data = data_loader.load_data(file_path)
    except FileNotFoundError:
        logging.info("File %s was not found", file_path)
        raise
    return worked_days_data


def transform_data(employee_records: list) -> list:
    parser = ParseWorkedDayData()
    return parser.parse(employee_records)


def calculate_payroll(worked_days_data: list):
    employee_salary: list = EmployeeSalary().compute_payroll(worked_days_data)
    return employee_salary


def save_payroll(payroll: list, file_name: str):
    DataSaverFactory().get_saver(DataFileSource.LOCAL_FOLDER).save(payroll, file_name)


def process_payroll(input_file_name: str, output_file_name: str):
    employee_records = load_data(input_file_name)
    parsed_employee_records: list = transform_data(employee_records)
    payroll: list = calculate_payroll(parsed_employee_records)
    save_payroll(payroll, output_file_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Error at least one parameter is required")
        print("Try python3 main.py -h")
        exit(-1)
    if sys.argv[1] in ("--help", "-h"):
        print(HELP_LINE)
        exit(0)

    worked_days_file_name: str = sys.argv[1]
    if not os.path.exists(worked_days_file_name):
        print("File %s was not found", worked_days_file_name)
        exit(-1)

    payroll_file_name: str = sys.argv[2] if sys.argv[2] is not None else "payroll.txt"

    process_payroll(worked_days_file_name, payroll_file_name)
