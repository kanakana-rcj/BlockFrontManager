"""Functions to update blockfront and neoforge to the latest version."""
from pathlib import Path

import requests

import getstatus
from config import BLOCKFRONT_PATH, NEOFORGE_PATH


def delete_old_blockfront(filename: str) -> None:
    """Delete old blockfront file which exicts in system.

    Args:
        filename: Name of the blockfront file to be deleted.

    """
    system_blockfront_filename = getstatus.get_system_blockfront_filename()

    if filename != system_blockfront_filename:
        print("delete old blockfront file")
        system_blockfront_path = BLOCKFRONT_PATH + "/" + system_blockfront_filename
        Path(system_blockfront_path).unlink()

def delete_old_neoforge(filename: str) -> None:
    """Delete old Neoforge installer file which exicts in system.

    Args:
        filename: Name of the Neoforge installer file to be deleted.

    """
    system_neoforge_filename = getstatus.get_system_neoforge_filename()

    if filename != system_neoforge_filename:
        print("delete old neoforge file")
        system_neoforge_path = NEOFORGE_PATH + "/" + system_neoforge_filename
        Path(system_neoforge_path).unlink()

def download_blockfront(url: str, filename: str) -> None:
    """Download blockfront file from given url.

    Args:
        url: URL of the blockfront file to be downloaded.
        filename: Name of the blockfront file to be deleted.

    """
    blockfront_file = requests.get(url, timeout=10, allow_redirects=True).content

    blockfront_path = BLOCKFRONT_PATH + "/" + filename
    with Path(blockfront_path).open("wb") as f:
        f.write(blockfront_file)
    print("saved blockfront to", blockfront_path)

def download_neoforge(url: str, filename: str) -> None:
    """Download neoforge installer file from given url.

    Args:
        url: URL of the neoforge installer file to be downloaded.
        filename: Name of the neoforge installer file to be deleted.

    """
    neoforge_file = requests.get(url, timeout=10, allow_redirects=True).content

    neoforge_path = NEOFORGE_PATH + "/" + filename
    with Path(neoforge_path).open("wb") as f:
        f.write(neoforge_file)
    print("saved neoforge to", neoforge_path)

def update() -> None:
    """Update blockfront to the latest version and neoforg to the required version."""
    blockfront_url = getstatus.get_latest_blockfront_url()
    blockfront_filename = getstatus.get_blockfront_filename_from_url(blockfront_url)

    delete_old_blockfront(blockfront_filename)

    print("getting latest blockfront file:", getstatus.get_blockfront_version_from_filename(blockfront_filename))
    download_blockfront(blockfront_url, blockfront_filename)

    neoforge_version = getstatus.get_required_neoforge_version()
    print("blockfront requires neoforge", neoforge_version)
    system_neoforge_version = getstatus.get_system_neoforge_version()
    print("system has neoforge", system_neoforge_version)

    if system_neoforge_version == neoforge_version:
        print("neoforge is up to date")

    else:
        print("neoforge needs to be updated")

        neoforge_url = getstatus.get_neoforge_url_from_version(neoforge_version)
        neoforge_filename = getstatus.get_neoforge_filename_from_version(neoforge_version)

        delete_old_neoforge(neoforge_filename)

        print("getting required neoforge file:", neoforge_version)
        download_neoforge(neoforge_url, neoforge_filename)
        print("Update is over. You should install neoforge from new installer now.")
        print("The neoforge installer is in :", NEOFORGE_PATH)
