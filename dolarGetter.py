from cronista import Cronista
from dolarhoy import DolarHoy
from lanacion import LaNacion
from urls import URLS

class DolarGetter():
  def __init__(self) -> None:
    self.dolarHoy = DolarHoy(URLS['DOLARHOY'])
    self.cronista = Cronista(URLS['CRONISTA'])
    self.la_nacion = LaNacion(URLS['LANACION'])
    
  def get_all(self):
    try:
      dolarHoy = self.dolarHoy.get_all()
      cronista = self.cronista.get_all()
      la_nacion = self.la_nacion.get_all()

      return {
        'dolar_hoy': dolarHoy,
        'cronista': cronista,
        'la_nacion': la_nacion
      }
    except:
      return None

  def get_blue(self):
    dolarHoyBlue = self.dolarHoy.get_dolar_blue()
    cronistaBlue = self.cronista.get_dolar_blue()
    la_nacionBlue = self.la_nacion.get_dolar_blue()

    blue = {
      'dolar_hoy': {
        'buy': dolarHoyBlue[0],
        'sell': dolarHoyBlue[1]
      },
      'cronista': {
        'buy': cronistaBlue[0],
        'sell': cronistaBlue[1]
      },
      'la_nacion': {
        'buy': la_nacionBlue[0],
        'sell': la_nacionBlue[1]
      }
    }
    
    return blue
  
  def get_oficial(self):
    dolarHoyOficial = self.dolarHoy.get_dolar_oficial()
    cronistaOficial = self.cronista.get_dolar_bna()
    la_nacionOficial = self.la_nacion.get_dolar_oficial()

    oficial = {
      'dolar_hoy': {
        'buy': dolarHoyOficial[0],
        'sell': dolarHoyOficial[1]
      },
      'cronista': {
        'buy': cronistaOficial[0],
        'sell': cronistaOficial[1]
      },
      'la_nacion': {
        'buy': la_nacionOficial[0],
        'sell': la_nacionOficial[1]
      }
    }

    return oficial

  def get_cll(self):
    dolar_hoy_ccl = self.dolarHoy.get_dolar_ccl()
    cronista_ccl = self.cronista.get_dolar_ccl()
    la_nacion_ccl = self.la_nacion.get_dolar_ccl()

    ccl = {
      'dolar_hoy': {
        'buy': dolar_hoy_ccl[0],
        'sell': dolar_hoy_ccl[1]
      },
      'cronista': {
        'buy': cronista_ccl[0],
        'sell': cronista_ccl[1]
      },
      'la_nacion': {          
        'sell': la_nacion_ccl
      }
    }
    return ccl




