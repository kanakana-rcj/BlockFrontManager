from abc import ABC

from pathlib import Path

import requests

class UpdaterBase(ABC):

    def delete_old_file(self, path: str) -> None:
        """Delete old file which exicts in system.

        Args:
            path: Path of the old file to be deleted.

        """
        file_path = Path(path)

        if file_path.exists():
            print("delete old file in:", path)
            file_path.unlink()
        else:
            print("file does not exists.")

    def download_file(self, url: str, path: str) -> None:
        """Download file from given url.

        Args:
            url: URL of the file to be downloaded.
            path: path of the file to be downloaded.

        """
        file = requests.get(url, timeout=10, allow_redirects=True).content
        file_path = Path(path)

        with file_path.open("wb") as f:
            f.write(file)

        print("saved file to: ", path)
