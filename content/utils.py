from bs4 import BeautifulSoup
import requests
from .summary import *


def get_page(url):
    resp = requests.get(url)
    return resp.content


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