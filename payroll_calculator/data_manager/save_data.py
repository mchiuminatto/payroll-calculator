import abc
import os

from payroll_calculator.data_manager.data_manager_types import DataFileSource


class DataSaver(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def save(records: list, file_name: str):
        ...


class LocalFolderSaver(DataSaver):
    """
    Manage saving a file in a local folder
    """

    @staticmethod
    def save(records: list, file_name: str):
        """
        Saves into a file, with file and folder pointed by "file_name",
        the records contained in the list "records"
        :param records: data to save
        :param file_name: file and folder name where to save the files

        :return:
        """

        folder: str = os.path.dirname(file_name)
        folder = "." if folder == "" else folder
        os.makedirs(folder, exist_ok=True)

        with open(file_name, "w", encoding="utf-8") as file_pointer:
            file_pointer.write("name, salary")
            for record in records:
                try:
                    file_pointer.write(f"\n{record['name']},{record['salary']}")
                except TypeError:
                    continue


class DataSaverFactory:
    """
    Subclass for saving payroll files in local folder
    """

    @staticmethod
    def get_saver(target_type: DataFileSource) -> DataSaver:
        """
        Factory to return DataSaver classes
        :param target_type:
        :return:
        """
        if target_type == DataFileSource.LOCAL_FOLDER:
            return LocalFolderSaver
