from fastapi import FastAPI, Depends, HTTPException, status
from dolarGetter import DolarGetter

app = FastAPI()

dolar_getter = DolarGetter()

# Crear una función de dependencia que retorna la instancia
def get_dolar_getter():
    return dolar_getter

@app.get('/')
async def root(dolar_getter: DolarGetter = Depends(get_dolar_getter)):
    try:
      all = dolar_getter.get_all()
      return all
    except Exception as e:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener los valores del dolar")

@app.get("/oficial")
async def get_dolar_oficial(dolar_getter: DolarGetter = Depends(get_dolar_getter)):
    try:
      oficial = dolar_getter.get_oficial()
      return oficial
    except:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el dolar oficial")

@app.get("/blue")
async def get_dolar_blue(dolar_getter: DolarGetter = Depends(get_dolar_getter)):
    try:
      blue = dolar_getter.get_blue()
      return blue
    except:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el dolar blue")
    
@app.get("/ccl")
async def get_dolar_ccl(dolar_getter: DolarGetter = Depends(get_dolar_getter)):
    try:
      cll = dolar_getter.get_cll()
      return cll
    except:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al obtener el dolar ccl (Contado con liqui)")


if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host='0.0.0.0', port=8000)


