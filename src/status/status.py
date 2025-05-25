"""Functions to get the status of blockfront and neoforge in the system and internet."""

from status.blockfront_status import BlockFrontStatus
from status.neoforge_status import NeoForgeStatus


class Status:

    def __init__(self) -> None:
        self.blockfront = BlockFrontStatus()
        self.neoforge = NeoForgeStatus()

    def get_status(self) -> None:
        """Get the status of blockfront and neoforge in the system and internet."""
        blockfront_url = self.blockfront.get_latest_url()
        print("latest blockfront URL:", blockfront_url)

        blockfront_filename = self.blockfront.get_filename_from_url(blockfront_url)
        print("blockfront latest file: ", blockfront_filename)

        blockfront_version = self.blockfront.get_version_from_filename(blockfront_filename)
        print("blockfront latest version: ", blockfront_version)
        print()

        required_neoforge_version = self.blockfront.get_required_neoforge_version()
        print("BlockFront requires NeoForge version:", required_neoforge_version)

        neoforge_url = self.neoforge.get_url_from_version(required_neoforge_version)
        print("required neoforge URL:", neoforge_url)

        neoforge_filename = self.neoforge.get_filename_from_version(required_neoforge_version)
        print("required neoforge filename:", neoforge_filename)
        print()

        system_blockfront_version = self.blockfront.get_system_version()
        print("system blockfront version:", system_blockfront_version)

        system_neoforge_version = self.neoforge.get_system_version()
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
