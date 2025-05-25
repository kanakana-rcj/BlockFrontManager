from config import NEOFORGE_PATH
from status.status_base import StatusBase


class NeoForgeStatus(StatusBase):

    def get_filename_from_url(self, url:str) -> str:
        index = 0
        for i in range(len(url)):
            if url[len(url)-1-i] == '/':
                index = len(url) - i
                break
        return url[index:]

    def get_filename_from_version(self, version:str) -> str | None:
        """Get the filename of neoforge installer from given version.

        Args:
            version: Version of the neoforge installer.

        Returns:
            Name of the neoforge installer.

        """
        if version:
            return "neoforge-" + version + "-installer.jar"
        return None

    def get_url_from_version(self, version:str) -> str | None:
        """Get the URL of required neoforge installer.

        Args:
            version: Version of the neoforge installer.

        Returns:
            URL of the required neoforge installer.

        """
        file_name = self.get_filename_from_version(version)
        if file_name:
            return "https://maven.neoforged.net/releases/net/neoforged/neoforge/" + version + "/" + file_name
        return None

    def get_version_from_filename(self, filename:str) -> str:
        """Get the version of neoforge installer from given filename.

        Args:
            filename: Name of the neoforge installer file.

        Returns:
            version: Version of the neoforge installer.

        """
        first_hyphen_index = filename.find("-")
        second_hyphen_index = filename.find("-", first_hyphen_index+1)  #1つめのハイフンの次から探す

        return filename[first_hyphen_index+1: second_hyphen_index]

    def get_system_version(self) -> str:
        """Get the version of neoforge installer in the system.

        Returns:
            version: Version of the neoforge installer in the system.

        """
        filename = self.get_system_filename(NEOFORGE_PATH, "neoforge")
        return self.get_version_from_filename(filename)
