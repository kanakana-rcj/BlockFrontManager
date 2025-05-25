"""Functions to update blockfront to the latest version."""
from config import BLOCKFRONT_PATH
from status.blockfront_status import BlockFrontStatus
from update.updater_base import UpdaterBase


class BlockFrontUpdater(UpdaterBase):

    def __init__(self) -> None:
        self.status = BlockFrontStatus()

    def update_blockfront(self) -> None:
        """Update blockfront to the latest version."""
        url = self.status.get_latest_url()
        new_filename = self.status.get_filename_from_url(url)

        old_filename = self.status.get_system_filename(BLOCKFRONT_PATH, "BlockFront")
        old_file_path = BLOCKFRONT_PATH + "/" + old_filename
        self.delete_old_file(old_file_path)

        print("getting latest blockfront version:", self.status.get_version_from_filename(new_filename))

        new_file_path = BLOCKFRONT_PATH + "/" + new_filename
        self.download_file(url, new_file_path)