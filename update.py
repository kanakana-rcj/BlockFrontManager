import requests
from dotenv import load_dotenv
import os 
import getstatus

load_dotenv()
BLOCKFRONT_DIR = os.environ.get("BLOCKFRONT_PATH")
NEOFORGE_DIR = os.environ.get("NEOFORGE_PATH")

def update():
    blockfront_url = getstatus.get_latest_blockfront_url()
    blockfront_filename = getstatus.get_blockfront_filename_from_url(blockfront_url)

    system_blockfront_filename = getstatus.get_system_blockfront_filename()

    if blockfront_filename != system_blockfront_filename:
        print("delete old blockfront file")
        system_blockfront_path = BLOCKFRONT_DIR + "/" + system_blockfront_filename
        os.remove(system_blockfront_path)

    print("getting latest blockfront file:", getstatus.get_blockfront_version_from_filename(blockfront_filename))
    blockfront_file = requests.get(blockfront_url, allow_redirects=True).content

    blockfront_path = BLOCKFRONT_DIR + "/" + blockfront_filename
    with open(blockfront_path, mode = 'wb') as f:
        f.write(blockfront_file)
    print("saved blockfront to", blockfront_path)

    neoforge_version = getstatus.get_required_neoforge_version()
    print("blockfront requires neoforge", neoforge_version)

    neoforge_url = getstatus.get_neoforge_url_from_version(neoforge_version)
    neoforge_filename = getstatus.get_neoforge_filename_from_version(neoforge_version)

    system_neoforge_filename = getstatus.get_system_neoforge_filename()

    if neoforge_filename != system_neoforge_filename:
        print("delete old neoforge file")
        system_neoforge_path = NEOFORGE_DIR + "/" + system_neoforge_filename
        os.remove(system_neoforge_path)

    print("getting required neoforge file:", neoforge_version)
    neoforge_file = requests.get(neoforge_url, allow_redirects=True).content

    neoforge_path = NEOFORGE_DIR + "/" + neoforge_filename
    with open(neoforge_path, mode = 'wb') as f:
        f.write(neoforge_file)
    print("saved neoforge to", neoforge_path)