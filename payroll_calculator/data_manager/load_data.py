import abc
from enum import Enum
import logging

from payroll_calculator.data_manager.data_manager_types import DataFileSource
class DataLoader(abc.ABC):

    def __init__(self, source_descriptor: dict):
        self.source_descriptor: dict = source_descriptor

    @abc.abstractmethod
    def load_data(self, file_name: str):
        pass


class LocalFolderLoader(DataLoader):
    """
    Loader for local folders files
    """

    def load_data(self, file_name: str) -> list[str]:
        with open(file_name, encoding="utf-8") as file_pointer:
            buffer: str = file_pointer.read()

        raw_data: list[str] = buffer.split("\n")

        return raw_data


class DataLoaderFactory:
    """
    Return instances of a data loader
    """

    def __init__(self,
                 file_source_type: DataFileSource,
                 source_descriptor: dict | None = None
                 ):
        self.file_source_type: DataFileSource = file_source_type
        self.source_descriptor = source_descriptor

    def get_loader(self):
        """
        Return the data loader from the specific type
        :return:
        """

        match self.file_source_type:
            case DataFileSource.LOCAL_FOLDER:
                return LocalFolderLoader(self.source_descriptor)
