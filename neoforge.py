import requests

print("enter neoforge version: ")
neoforge_version = input()

neoforge_url = "https://maven.neoforged.net/releases/net/neoforged/neoforge/" + neoforge_version + "/neoforge-" + neoforge_version + "-installer.jar"
filename = "neoforge-" + neoforge_version + "-installer.jar"

print("neoforge URL:", neoforge_url)

neoforge_installer = requests.get(neoforge_url, allow_redirects=True).content
with open(filename, mode='wb') as f:
    f.write(neoforge_installer)