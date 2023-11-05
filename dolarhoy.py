from scrapper import Scrapper
from utils import parseValue

class DolarHoy(Scrapper):
  def __init__(self, url) -> None:
    self.url = url
    self.soup = self.get_soup()
    pass

  def get_all(self):
    try:
      blue = self.get_dolar_blue()
      oficial = self.get_dolar_oficial()
      bolsa = self.get_dolar_bolsa()
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
        'bolsa': {
          'buy': bolsa[0],
          'sell': bolsa[1]
        },
        'ccl': {
          'buy': ccl[0],
          'sell': ccl[1]
        }
      }
    except:
      return None

  def get_dolar_blue(self):
    try:
      dolar_blue_container = self.soup.find('a', href = '/cotizaciondolarblue').find_parent('div', class_ = 'tile is-child')  
      blue_buy = dolar_blue_container.find('div', class_ = 'compra').find('div', class_='val')
      blue_sell = dolar_blue_container.find('div', class_ = 'venta').find('div', class_='val')

      buy_value = parseValue(blue_buy)
      sell_value = parseValue(blue_sell)

      return buy_value, sell_value
    except:
      return None, None

  def get_dolar_oficial(self):
    try:
      dolar_oficial_container = self.soup.find('a', href = '/cotizaciondolaroficial').find_parent('div', class_ = 'tile is-child')
      oficial_buy = dolar_oficial_container.find('div', class_ = 'compra').find('div', class_='val')
      oficial_sell = dolar_oficial_container.find('div', class_ = 'venta').find('div', class_='val')

      buy_value = parseValue(oficial_buy)
      sell_value = parseValue(oficial_sell)

      return buy_value, sell_value
    except:
      return None, None
  
  def get_dolar_bolsa(self):
    try:
      dolar_bolsa_container = self.soup.find('a', href = '/cotizaciondolarbolsa').find_parent('div', class_ = 'tile is-child')
      bolsa_buy = dolar_bolsa_container.find('div', class_ = 'compra').find('div', class_='val')
      bolsa_sell = dolar_bolsa_container.find('div', class_ = 'venta').find('div', class_='val')

      buy_value = parseValue(bolsa_buy)
      sell_value = parseValue(bolsa_sell)

      return buy_value, sell_value
    except:
      return None, None
  
  def get_dolar_ccl(self):
    try:
      dolar_ccl_container = self.soup.find('a', href = '/cotizaciondolarcontadoconliqui').find_parent('div', class_ = 'tile is-child')
      ccl_buy = dolar_ccl_container.find('div', class_ = 'compra').find('div', class_='val')
      ccl_sell = dolar_ccl_container.find('div', class_ = 'venta').find('div', class_='val')

      buy_value = parseValue(ccl_buy)
      sell_value = parseValue(ccl_sell)

      return buy_value, sell_value
    except:
      return None, None
    
  def get_all(self):
    try:
      blue = self.get_dolar_blue()
      oficial = self.get_dolar_oficial()
      bolsa = self.get_dolar_bolsa()
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
        'bolsa': {
          'buy': bolsa[0],
          'sell': bolsa[1]
        },
        'ccl': {
          'buy': ccl[0],
          'sell': ccl[1]
        }
      }
    except:
      return None
