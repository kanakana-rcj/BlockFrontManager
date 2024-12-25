import requests
from dotenv import load_dotenv
import os 
import getstatus

load_dotenv()
BLOCKFRONT_DIR = os.environ.get("BLOCKFRONT_PATH")
NEOFORGE_DIR = os.environ.get("NEOFORGE_PATH")

def delete_old_blockfront(filename):
    system_blockfront_filename = getstatus.get_system_blockfront_filename()

    if filename != system_blockfront_filename:
        print("delete old blockfront file")
        system_blockfront_path = BLOCKFRONT_DIR + "/" + system_blockfront_filename
        os.remove(system_blockfront_path)

def delete_old_neoforge(filename):
    system_neoforge_filename = getstatus.get_system_neoforge_filename()

    if filename != system_neoforge_filename:
        print("delete old neoforge file")
        system_neoforge_path = NEOFORGE_DIR + "/" + system_neoforge_filename
        os.remove(system_neoforge_path)

def download_blockfront(url, filename):
    blockfront_file = requests.get(url, allow_redirects=True).content

    blockfront_path = BLOCKFRONT_DIR + "/" + filename
    with open(blockfront_path, mode = 'wb') as f:
        f.write(blockfront_file)
    print("saved blockfront to", blockfront_path)

def download_neoforge(url, filename):
    neoforge_file = requests.get(url, allow_redirects=True).content

    neoforge_path = NEOFORGE_DIR + "/" + filename
    with open(neoforge_path, mode = 'wb') as f:
        f.write(neoforge_file)
    print("saved neoforge to", neoforge_path)

def update():
    blockfront_url = getstatus.get_latest_blockfront_url()
    blockfront_filename = getstatus.get_blockfront_filename_from_url(blockfront_url)

    delete_old_blockfront(blockfront_filename)

    print("getting latest blockfront file:", getstatus.get_blockfront_version_from_filename(blockfront_filename))
    download_blockfront(blockfront_url, blockfront_filename)

    neoforge_version = getstatus.get_required_neoforge_version()
    print("blockfront requires neoforge", neoforge_version)

    neoforge_url = getstatus.get_neoforge_url_from_version(neoforge_version)
    neoforge_filename = getstatus.get_neoforge_filename_from_version(neoforge_version)

    delete_old_neoforge(neoforge_filename)

    print("getting required neoforge file:", neoforge_version)
    download_neoforge(neoforge_url, neoforge_filename)