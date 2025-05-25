"""Functions to update neoforge to the latest version."""
from neoforge_status import NeoForgeStatus
from config import NEOFORGE_PATH
from updater_base import UpdaterBase
from blockfront_status import BlockFrontStatus

class NeoForgeUpdater(UpdaterBase):

    def __init__(self) -> None:
        self.neo_status = NeoForgeStatus()
        self.bf_status = BlockFrontStatus()

    def update_neoforge(self) -> None:
        """Update neoforg to the required version."""
        new_version = self.bf_status.get_required_neoforge_version()
        print("blockfront requires neoforge", new_version)
        old_version = self.neo_status.get_system_version()
        print("system has neoforge", old_version)

        if old_version == new_version:
            print("neoforge is up to date")

        else:
            print("neoforge needs to be updated")

            url = self.neo_status.get_url_from_version(new_version)
            new_filename = self.neo_status.get_filename_from_version(new_version)

            old_file_path = NEOFORGE_PATH + "/" + self.neo_status.get_system_filename(NEOFORGE_PATH, "neoforge")
            self.delete_old_file(old_file_path)

            print("getting required neoforge file:", new_version)

            new_file_path = NEOFORGE_PATH + "/" + new_filename
            self.download_file(url, new_file_path)
            print("Update is over. You should install neoforge from new installer now.")
            print("The neoforge installer is in :", new_file_path)