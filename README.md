# API de Cotizacion de Dolar en Argentina

## Descripcion

Este proyecto es una API que permite obtener la cotizacion del dolar en Argentina de distintas fuentes.

**Cronista**: https://www.cronista.com/
**Dolar Hoy**: https://www.dolarhoy.com/
**La Nacion**: https://www.lanacion.com.ar

## Instalacion

Para instalar el proyecto se debe realizar lo siguiente:

1. Instalar la ultima version de Python 3.
2. Clonar el repositorio.

```bash
  git clone
```

3. Crear un entorno virtual.

```bash
  python -m venv venv
```

4. Activar el entorno virtual.

```bash
  source venv/bin/activate
```

5. Instalar las dependencias.

```bash
  pip install -r requirements.txt
```

6. Ejecutar api

```bash
  uvicorn main:app --reload
```

7. Abrir el navegador y acceder a la siguiente URL: http://localhost:8000
