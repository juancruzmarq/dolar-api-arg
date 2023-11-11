from scrapper import Scrapper
from utils import parseValue

class Cronista(Scrapper):
  def __init__(self, url) -> None:
    super().__init__(url)
    self.url = url
    self.soup = self.get_soup()
    self.html = self.get_html()
    self.table_dolar_values= self.get_table_dolar()
    pass

  def get_all(self):
    blue = self.get_dolar_blue()
    oficial = self.get_dolar_bna()
    turista = self.get_dolar_turista()
    mep = self.get_dolar_mep()
    ccl = self.get_dolar_ccl()

    return {
      'blue': {
        'buy': blue[0],
        'sell': blue[1]
      },
      'oficial': {
        'buy': oficial[0],
        'sell': oficial[1]
      },
      'turista': {
        'buy': turista[0],
        'sell': turista[1]
      },
      'mep': {
        'buy': mep[0],
        'sell': mep[1]
      },
      'ccl': {
        'buy': ccl[0],
        'sell': ccl[1]
      }
    }

  def get_table_dolar(self):
    try:
      print(self.soup)
      table = self.soup.find('table', {'id': 'market-scrll-2'})
      print(table)
      rows = table.find_all('tr')
      dolar_values = {}
      for row in rows:
        cells = row.find_all('td')
        if cells:
          dolar_type = cells[0].get_text(strip=True).lower().split(' ')[1]
          buy_value = float(cells[1].find('div', class_='buy-value').get_text(strip=True).replace('$', '').replace(',', '.'))
          sell_value = float(cells[2].find('div', class_='sell-value').get_text(strip=True).replace('$', '').replace(',', '.'))
          dolar_values[dolar_type] = {'Compra': buy_value, 'Venta': sell_value}
      return dolar_values
    except:
      return None


  def get_dolar_blue(self):
    buy_value = self.table_dolar_values['blue']['Compra']
    sell_value = self.table_dolar_values['blue']['Venta']
    return buy_value, sell_value

  def get_dolar_bna(self):
    buy_value = self.table_dolar_values['bna']['Compra']
    sell_value = self.table_dolar_values['bna']['Venta']
    return buy_value, sell_value
  
  def get_dolar_mep(self):
    buy_value = self.table_dolar_values['mep']['Compra']
    sell_value = self.table_dolar_values['mep']['Venta']
    return buy_value, sell_value
  
  def get_dolar_ccl(self):
    buy_value = self.table_dolar_values['ccl']['Compra']
    sell_value = self.table_dolar_values['ccl']['Venta']
    return buy_value, sell_value
  
  def get_dolar_turista(self):
    buy_value = self.table_dolar_values['turista']['Compra']
    sell_value = self.table_dolar_values['turista']['Venta']
    return buy_value, sell_value
  