from bs4 import BeautifulSoup
import requests

class Scrapper:
  def __init__(self, url) -> None:
    self.url = url
    pass

  def get_html(self, url = None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    req = requests.get(self.url if url is None else url, headers=headers)
    html = req.text
    return html
  
  def get_soup(self, html = None):
    html = self.get_html() if html is None else html
    soup = BeautifulSoup(html, 'html.parser')
    return soup
  
  