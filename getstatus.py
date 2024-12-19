import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()
BLOCKFRONT_PATH = os.environ.get("BLOCKFRONT_PATH")
NEOFORGE_PATH = os.environ.get("NEOFORGE_PATH")

def get_latest_blockfront_url():
    url = 'https://modrinth.com/mod/blockfront/versions'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #arial-label : Download　の aタグの中で最初のものを取得
    a_tag = soup.find('a', {'aria-label': 'Download'})

    if a_tag:
        latest_blockfront_url = a_tag.get('href')
        return latest_blockfront_url
    else:
        print("<a> tag not found")

def get_neoforge_url_from_version(version:str):
    url = "https://maven.neoforged.net/releases/net/neoforged/neoforge/" + version + "/neoforge-" + version + "-installer.jar"
    return url

def get_blockfront_filename_from_url(url:str):
    versionid_len = 8
    versionid_end_index = url.find("versions") - 1 + len("versions/") + versionid_len + len('/')
    filename = url[versionid_end_index + 1:]
    return filename

def get_neoforge_filename_from_version(version:str):
    filename = "neoforge-" + version + "-installer.jar"
    return filename

def get_neoforge_version_from_filename(filename:str):
    first_hyphen_index = filename.find('-')  
    second_hyphen_index = filename.find('-', first_hyphen_index+1) #1つめのハイフンの次から探す

    version = filename[first_hyphen_index+1: second_hyphen_index]
    return version

def get_required_neoforge_version():
    url = "https://modrinth.com/mod/blockfront/changelog"
    response = requests.get(url)
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

def get_blockfront_version_from_filename(filename:str):
    second_hyphen_index = filename.find('-', len("BlockFront-"))  
    third_hyphen_index = filename.find('-', second_hyphen_index+1) #2つめのハイフンの次から探す
    version = filename[second_hyphen_index+1: third_hyphen_index]
    return version

def get_system_blockfront_version():
    files = os.listdir(BLOCKFRONT_PATH)
    blockfront_index = 0
    for i in range(len(files)):
        if files[i].find("BlockFront") != -1:
            blockfront_index = i
            break
        else: 
            if i == len(files) - 1:
                print("BlockFront was not found in your system")
                break
    version = get_blockfront_version_from_filename(files[blockfront_index])
    return version

def get_system_neoforge_version():
    files = os.listdir(NEOFORGE_PATH)
    neoforge_index = 0
    for i in range(len(files)):
        if files[i].find("neoforge") != -1:
            neoforge_index = i
            break
        else:
            if i == len(files) - 1:
                print("NeoForge was not found in your system")
                break
    version = get_neoforge_version_from_filename(files[neoforge_index])
    return version
    
if __name__ == "__main__":
    
    blockfront_url = get_latest_blockfront_url()
    print("latest blockfront URL:", blockfront_url)

    blockfront_filename = get_blockfront_filename_from_url(blockfront_url)
    print("blockfront latest file: ", blockfront_filename)

    blockfront_version = get_blockfront_version_from_filename(blockfront_filename)
    print("blockfront latest version: ", blockfront_version)
    print("")

    required_neoforge_version = get_required_neoforge_version()
    print("BlockFront requires NeoForge version:", required_neoforge_version)

    neoforge_url = get_neoforge_url_from_version(required_neoforge_version)
    print("required neoforge URL:", neoforge_url)

    neoforge_filename = get_neoforge_filename_from_version(required_neoforge_version)
    print("required neoforge filename:", neoforge_filename)
    print("")

    system_blockfront_version = get_system_blockfront_version()
    print("system blockfront version:", system_blockfront_version)

    system_neoforge_version = get_system_neoforge_version()
    print("system neoforge version:", system_neoforge_version)
    print("")

    if system_blockfront_version == blockfront_version:
        print("BlockFront is up to date")
    else:
        print("BlockFront needs to be updated")
    
    if system_neoforge_version == required_neoforge_version:
        print("NeoForge is up to date")
    else: 
        print("NeoForge needs to be updated")