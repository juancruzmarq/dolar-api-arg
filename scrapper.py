from bs4 import BeautifulSoup
import requests

class Scrapper:
  def __init__(self, url) -> None:
    self.url = url
    pass

  def get_html(self, url = None):
    req = requests.get(self.url if url is None else url)
    html = req.text
    return html
  
  def get_soup(self, html = None):
    html = self.get_html() if html is None else html
    soup = BeautifulSoup(html, 'html.parser')
    return soup
  
  