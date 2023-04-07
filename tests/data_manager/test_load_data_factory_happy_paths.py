from payroll_calculator import constants
from payroll_calculator.data_manager.load_data import DataLoaderFactory, LocalFolderLoader
from payroll_calculator.data_manager.load_data import DataFileSource

DATA_FOLDER_PATH = constants.ROOT_DIR + "/tests/data_manager/"


def test_load_local_folder_file():
    local_folder_loader: LocalFolderLoader = DataLoaderFactory(file_source_type=DataFileSource.LOCAL_FOLDER,
                                                               source_descriptor={
                                                                   "folder": DATA_FOLDER_PATH}).get_loader()
    data: list = local_folder_loader.load_data(DATA_FOLDER_PATH+"work_days_1.txt")
    names: list = ["RENE", "ASTRID"]
    for line in data:
        assert line.split("=")[0] == names.pop(0)


def test_manage_heavy_load(gen_dummy_data):
    gen_dummy_data()
    loader: LocalFolderLoader = DataLoaderFactory(file_source_type=DataFileSource.LOCAL_FOLDER,
                                                  source_descriptor={"folder": DATA_FOLDER_PATH}).get_loader()
    data: list = loader.load_data("workdays_heavy.txt")
    assert len(data) == constants.TEST_RECORDS
