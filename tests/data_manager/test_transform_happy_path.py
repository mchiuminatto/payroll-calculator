import re
from payroll_calculator import constants
from payroll_calculator.data_manager.transformations import ParseWorkedDayData
from payroll_calculator.payroll.payroll_calculator import WeekDays
from payroll_calculator.data_manager.load_data import DataLoaderFactory, LocalFolderLoader, DataFileSource

test_record = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"

DATA_FOLDER_PATH = constants.ROOT_DIR + "/tests/data_manager/"


def test_parse_workday_record():
    employee_record: dict = ParseWorkedDayData().parse_worked_day_record(test_record)
    assert employee_record["name"] == "RENE"
    for worked_day in employee_record["data"]:
        assert type(worked_day["weekday"]) is WeekDays


def test_parse_multiple(gen_dummy_data):
    gen_dummy_data()
    local_folder_loader: LocalFolderLoader = DataLoaderFactory(file_source_type=DataFileSource.LOCAL_FOLDER,
                                                               source_descriptor={
                                                                   "folder": DATA_FOLDER_PATH}).get_loader()
    employee_records: list = local_folder_loader.load_data("workdays_heavy.txt")

    for employee_record in employee_records:
        parser = ParseWorkedDayData()
        parsed_record: dict = parser.parse_worked_day_record(employee_record)
        assert re.match(r"[A-Z]+", parsed_record["name"]) is not None


def test_full_transform(gen_dummy_data):
    gen_dummy_data()

    local_folder_loader: LocalFolderLoader = DataLoaderFactory(file_source_type=DataFileSource.LOCAL_FOLDER,
                                                               source_descriptor={
                                                                   "folder": DATA_FOLDER_PATH}).get_loader()
    employee_records: list = local_folder_loader.load_data("workdays_heavy.txt")

    parser = ParseWorkedDayData()
    parsed_employee_records: list = parser.parse(employee_records)
    for employee_record in parsed_employee_records:
        assert re.match(r"[A-Z]+", employee_record["name"]) is not None
