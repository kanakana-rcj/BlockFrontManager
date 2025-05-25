"""Functions to get the status of blockfront in the system and internet."""
import requests
from bs4 import BeautifulSoup

from config import BLOCKFRONT_PATH
from status.status_base import StatusBase


class BlockFrontStatus(StatusBase):

    def get_latest_url(self) -> str | None:
        """Get the URL of latest blockfront from modrinth.

        Returns:
            URL of the latest blockfront version.

        """
        url = "https://modrinth.com/mod/blockfront/versions"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        a_tag = soup.find("a", {"aria-label": "Download"})

        if a_tag:
            return a_tag.get("href")
        print("<a> tag not found")
        return None

    def get_filename_from_url(self, url:str) -> str:
        """Get the filename of blockfront from given URL.

        Args:
            url: URL of the blockfront file.

        Returns:
            Name of the blockfront file.

        """
        versionid_len = 8
        versionid_end_index = url.find("versions") - 1 + len("versions/") + versionid_len + len("/")
        return url[versionid_end_index + 1:]

    def get_filename_from_version(self, version:str) -> str | None:
        url = "https://modrinth.com/mod/blockfront/version/" + version
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        span_tag = soup.select_one('h4:contains("Game versions") ~ span')
        if span_tag:
            minecraft_version = span_tag.contents[0]
            return "BlockFront-" + minecraft_version + "-" + version + "-RELEASE.jar"
        return None

    def get_url_from_version(self, version:str) -> str | None:

        url = "https://modrinth.com/mod/blockfront/version/" + version
        filename = self.get_filename_from_version(version)
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        a_tag = soup.find("a", {"title": "Download " + filename})
        if a_tag:
            return a_tag.get("href")
        print("<a> tag not found")
        return None

    def get_version_from_filename(self, filename:str) -> str:
        """Get the version of blockfront from given filename.

        Args:
            filename: Name of the blockfront file.

        Returns:
            version: Version of the blockfront.

        """
        second_hyphen_index = filename.find("-", len("BlockFront-"))
        third_hyphen_index = filename.find("-", second_hyphen_index+1) #2つめのハイフンの次から探す
        return filename[second_hyphen_index+1: third_hyphen_index]

    def get_system_version(self) -> str:
        """Get the version of blockfront in the system.

        Returns:
            version: Version of the blockfront in the system.

        """
        filename = self.get_system_filename(BLOCKFRONT_PATH, "BlockFront")
        return self.get_version_from_filename(filename)

    def get_required_neoforge_version(self) -> str:
        """Get the version of neoforge which is required by blockfront from modrinth.

        Returns:
            required_neoforge_version: Version of neoforge required by blockfront.

        """
        url = "https://modrinth.com/mod/blockfront/changelog"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        matching_tags = soup.find_all(string=lambda text: "NeoForge" in text if text else False)

        required_neoforge_version = ""
        for tag in matching_tags:
            if tag.find("Updated to the latest") != -1:
                open_parenthesis_index = tag.find("(")
                close_parenthesis_index = tag.find(")")
                required_neoforge_version = tag[open_parenthesis_index+1:close_parenthesis_index]
                break
        return required_neoforge_version