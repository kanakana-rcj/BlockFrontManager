"""Functions to update blockfront and neoforge to the latest version."""

from update.update_blockfront import BlockFrontUpdater
from update.update_neoforge import NeoForgeUpdater


class Updater:

    def __init__(self) -> None:
        self.blockfront_updater = BlockFrontUpdater()
        self.neoforge_updater = NeoForgeUpdater()

    def update(self) -> None:
        """Update blockfront and neoforg."""
        self.blockfront_updater.update_blockfront()
        self.neoforge_updater.update_neoforge()