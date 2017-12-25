from bs4 import BeautifulSoup
import urllib3
from .summary import *


def get_page(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data


def get_properties(content):
    soup = BeautifulSoup(content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    result = " ".join(soup.stripped_strings)
    image = None
    if soup.find(itemprop="image"):
        image_meta = soup.find(itemprop="image").find('meta')
        image = image_meta.attrs['content'] if image_meta else None
    return soup.title.string, result, summarize(result), image