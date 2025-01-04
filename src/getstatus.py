"""Functions to get the status of blockfront and neoforge in the system and internet."""
import os

import requests
from bs4 import BeautifulSoup

from config import BLOCKFRONT_PATH, NEOFORGE_PATH


def get_latest_blockfront_url() -> str | None:
    """Get the URL of latest blockfront from modrinth.

    Returns:
        URL of the latest blockfront version.

    """
    url = "https://modrinth.com/mod/blockfront/versions"
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    #arial-label : Download　の aタグの中で最初のものを取得
    a_tag = soup.find("a", {"aria-label": "Download"})

    if a_tag:
        return a_tag.get("href")
    print("<a> tag not found")
    return None

def get_neoforge_url_from_version(version:str) -> str:
    """Get the URL of required neoforge installer.

    Args:
        version: Version of the neoforge installer.

    Returns:
        URL of the required neoforge installer.

    """
    return "https://maven.neoforged.net/releases/net/neoforged/neoforge/" + version + "/neoforge-" + version + "-installer.jar"

def get_blockfront_filename_from_url(url:str) -> str:
    """Get the filename of blockfront from given URL.

    Args:
        url: URL of the blockfront file.

    Returns:
        Name of the blockfront file.

    """
    versionid_len = 8
    versionid_end_index = url.find("versions") - 1 + len("versions/") + versionid_len + len("/")
    return url[versionid_end_index + 1:]

def get_neoforge_filename_from_version(version:str) -> str:
    """Get the filename of neoforge installer from given version.

    Args:
        version: Version of the neoforge installer.

    Returns:
        Name of the neoforge installer.

    """
    return "neoforge-" + version + "-installer.jar"

def get_neoforge_version_from_filename(filename:str) -> str:
    """Get the version of neoforge installer from given filename.

    Args:
        filename: Name of the neoforge installer file.

    Returns:
        version: Version of the neoforge installer.

    """
    first_hyphen_index = filename.find("-")
    second_hyphen_index = filename.find("-", first_hyphen_index+1)  #1つめのハイフンの次から探す

    return filename[first_hyphen_index+1: second_hyphen_index]

def get_required_neoforge_version() -> str:
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

def get_blockfront_version_from_filename(filename:str) -> str:
    """Get the version of blockfront from given filename.

    Args:
        filename: Name of the blockfront file.

    Returns:
        version: Version of the blockfront.

    """
    second_hyphen_index = filename.find("-", len("BlockFront-"))
    third_hyphen_index = filename.find("-", second_hyphen_index+1) #2つめのハイフンの次から探す
    return filename[second_hyphen_index+1: third_hyphen_index]

def get_system_blockfront_filename() -> list[str]:
    """Get the filename of blockfront in the system.

    Returns:
        files: List of filenames in the mod directory.

    """
    files = os.listdir(BLOCKFRONT_PATH)
    blockfront_index = 0
    for i in range(len(files)):
        if files[i].find("BlockFront") != -1:
            blockfront_index = i
            break

        if i == len(files) - 1:
            print("BlockFront was not found in your system")
            break

    return files[blockfront_index]

def get_system_blockfront_version() -> str:
    """Get the version of blockfront in the system.

    Returns:
        version: Version of the blockfront in the system.

    """
    filename = get_system_blockfront_filename()
    return get_blockfront_version_from_filename(filename)

def get_system_neoforge_filename() -> list[str]:
    """Get the filename of neoforge installer in the system.

    Returns:
        files: List of filenames in the directory which neoforge exicts.

    """
    files = os.listdir(NEOFORGE_PATH)
    neoforge_index = 0
    for i in range(len(files)):
        if files[i].find("neoforge") != -1:
            neoforge_index = i
            break

        if i == len(files) - 1:
            print("NeoForge was not found in your system")
            break

    return files[neoforge_index]

def get_system_neoforge_version() -> str:
    """Get the version of neoforge installer in the system.

    Returns:
        version: Version of the neoforge installer in the system.

    """
    filename = get_system_neoforge_filename()
    return get_neoforge_version_from_filename(filename)

def get_status() -> None:
    """Get the status of blockfront and neoforge in the system and internet."""
    blockfront_url = get_latest_blockfront_url()
    print("latest blockfront URL:", blockfront_url)

    blockfront_filename = get_blockfront_filename_from_url(blockfront_url)
    print("blockfront latest file: ", blockfront_filename)

    blockfront_version = get_blockfront_version_from_filename(blockfront_filename)
    print("blockfront latest version: ", blockfront_version)
    print()

    required_neoforge_version = get_required_neoforge_version()
    print("BlockFront requires NeoForge version:", required_neoforge_version)

    neoforge_url = get_neoforge_url_from_version(required_neoforge_version)
    print("required neoforge URL:", neoforge_url)

    neoforge_filename = get_neoforge_filename_from_version(required_neoforge_version)
    print("required neoforge filename:", neoforge_filename)
    print()

    system_blockfront_version = get_system_blockfront_version()
    print("system blockfront version:", system_blockfront_version)

    system_neoforge_version = get_system_neoforge_version()
    print("system neoforge version:", system_neoforge_version)
    print()

    if system_blockfront_version == blockfront_version:
        print("BlockFront is up to date")
    else:
        print("BlockFront needs to be updated")

    if system_neoforge_version == required_neoforge_version:
        print("NeoForge is up to date")
    else: 
        print("NeoForge needs to be updated")
