from scrapper import Scrapper

class LaNacion(Scrapper):
  def __init__(self, url) -> None:
    super().__init__(url)
    self.soup = self.get_soup()
    self.html = self.get_html()

  def get_all(self):
    try:
      blue = self.get_dolar_blue()
      oficial = self.get_dolar_oficial()
      tarjeta = self.get_dolar_tarjeta()
      turista = self.get_dolar_turista()
      mep = self.get_dolar_mep()
      ccl = self.get_dolar_ccl()
      mayorista = self.get_dolar_mayorista()
      
      return {
        'blue': {
          'buy': blue[0],
          'sell': blue[1]
        },
        'oficial': {
          'buy': oficial[0],
          'sell': oficial[1]
        },
        'tarjeta': {
          'sell': tarjeta
        },
        'turista': {
          'sell': turista
        },
        'mep': {
          'sell': mep
        },
        'ccl': {
          'sell': ccl
        },
        'mayorista': {
          'sell': mayorista
        }
      }
    except:
      return None

  def get_dolar_blue(self):
    dolar_blue_container = self.soup.find('a', href='https://www.lanacion.com.ar/tema/dolar-blue-tid67294/').find_parent('div', class_ = 'currency-data')
    values = dolar_blue_container.find_all('strong', class_ = '--fourxs')
    buy_value = float(values[0].get_text(strip=True).replace(',', '.').replace('$', ''))
    sell_value = float(values[1].get_text(strip=True).replace(',', '.').replace('$', ''))
    
    return buy_value, sell_value
  
  def get_dolar_oficial(self):
    dolar_oficial_container = self.soup.find('a', attrs={'title': 'Dólar oficial'}).find_parent('div', class_ = 'currency-data')
    values = dolar_oficial_container.find_all('strong', class_ = '--fourxs')

    buy_value = float(values[0].get_text(strip=True).replace(',', '.').replace('$', ''))
    sell_value = float(values[1].get_text(strip=True).replace(',', '.').replace('$', ''))
    
    return buy_value, sell_value

  def get_dolar_tarjeta(self):
    dolar_tarjeta_container = self.soup.find('a', attrs={'title': 'Dólar tarjeta'}).find_parent('div', class_ = 'currency-data')
    values = dolar_tarjeta_container.find_all('strong', class_ = '--fourxs')
    sell_value = float(values[0].get_text(strip=True).replace(',', '.').replace('$', ''))

    return sell_value
  
  def get_dolar_turista(self):
    dolar_turista_container = self.soup.find('a', attrs={'title': 'Dólar turista'}).find_parent('div', class_ = 'currency-data')
    values = dolar_turista_container.find_all('strong', class_ = '--fourxs')
    sell_value = float(values[0].get_text(strip=True).replace(',', '.').replace('$', ''))

    return sell_value
  
  def get_dolar_mep(self):
    dolar_mep_strong_tag = self.soup.find('h2', string='Dólar MEP').find_next('strong')
    dolar_mep_value = float(''.join(dolar_mep_strong_tag.stripped_strings).replace(',', '.').replace('$', ''))

    return dolar_mep_value
  
  def get_dolar_ccl(self):
    dolar_ccl_container = self.soup.find('a', attrs={'title': 'Dólar CCL'}).find_parent('div', class_ = 'currency-data')
    values = dolar_ccl_container.find_all('strong', class_ = '--fourxs')
    sell_value = float(values[0].get_text(strip=True).replace(',', '.').replace('$', ''))

    return sell_value
  
  def get_dolar_mayorista(self):
    dolar_mayorista_strong_tag = self.soup.find('h2', string='Dólar mayorista').find_next('strong')
    dolar_mayorista_value = float(''.join(dolar_mayorista_strong_tag.stripped_strings).replace(',', '.').replace('$', ''))

    return dolar_mayorista_value
  

    
