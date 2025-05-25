import os
from abc import ABC, abstractmethod


class StatusBase(ABC):
    @abstractmethod
    def get_filename_from_url(self, url:str) -> str:
        pass

    @abstractmethod
    def get_filename_from_version(self, version:str) -> str | None:
        pass

    @abstractmethod
    def get_url_from_version(self, version:str) -> str | None:
        pass

    @abstractmethod
    def get_version_from_filename(self, filename:str) -> str:
        pass

    @abstractmethod
    def get_system_version(self) -> str:
        pass

    def get_system_filename(self, path: str, keyword: str) -> str:
        """Get the filename in the system.

        Returns:
            files: Name of the file in the system.

        """
        files = os.listdir(path)
        for file in files:
            if keyword in file:
                return file

        print(f"{keyword} was not found in your system")
        return ""