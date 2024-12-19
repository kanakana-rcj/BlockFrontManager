import requests
from bs4 import BeautifulSoup
import re

url = 'https://modrinth.com/mod/blockfront/versions'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#arial-label : Download　の aタグの中で最初のものを取得
a_tag = soup.find('a', {'aria-label': 'Download'})

if a_tag:
    latest_modfile_url = a_tag.get('href')
    print("latest modfile URL of blockfront:", latest_modfile_url)
    
    match = re.search(r"BlockFront-.*", latest_modfile_url)
    filename = match.group()
    print("blockfront modfile name: ", filename)
    
    modfile = requests.get(latest_modfile_url, allow_redirects=True).content
    with open(filename , mode = 'wb') as f:
        f.write(modfile)
    
else:
    print("<a> tag not found")

