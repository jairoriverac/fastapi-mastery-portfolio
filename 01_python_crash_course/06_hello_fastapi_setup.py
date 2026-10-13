"""
SUBTEMA 06: Primer Servidor FastAPI, Decoradores ASGI y Swagger UI
------------------------------------------------------------------
Teoría breve (del video de HolaMundo [00:07:25 - 00:12:42]):
Al instanciar `app = FastAPI()`, creamos una aplicación compatible con la especificación ASGI
(Asynchronous Server Gateway Interface). FastAPI toma los diccionarios retornados por
las funciones y los serializa a JSON estándar automáticamente. Además, inspecciona la firma
de la función y genera la documentación OpenAPI accesible en `/docs`.
"""

from typing import Any
from fastapi import FastAPI, status

# 1. Instanciación de la aplicación FastAPI con metadata para OpenAPI
app = FastAPI(
    title="01 - Hello FastAPI & Python Express",
    description="Primer servidor demostrativo con endpoints síncronos y asíncronos.",
    version="1.0.0",
)


# 2. Endpoint Raíz (GET): Retorna un diccionario serializado automáticamente a JSON
@app.get(
    "/",
    status_code=status.HTTP_200_OK,
    tags=["General"],
    summary="Endpoint de bienvenida",
)
def home() -> dict[str, str]:
    """Retorna un saludo JSON básico."""
    return {"mensaje": "Hola mundo desde FastAPI!"}


# 3. Endpoint Asíncrono (async def): Ideal para llamadas I/O
@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    tags=["Observabilidad"],
    summary="Health check del servicio",
)
async def health_check() -> dict[str, Any]:
    """Verifica el estado del servicio y su tiempo de actividad."""
    return {
        "status": "healthy",
        "service": "fastapi-mastery-portfolio",
        "version": "1.0.0",
    }


# =====================================================================
# 💡 TIPS DE USO Y BUENAS PRÁCTICAS:
# 1. Cómo correr este archivo en desarrollo:
#    $ fastapi dev 01_python_crash_course/06_hello_fastapi_setup.py
# 2. Visita en tu navegador:
#    - http://127.0.0.1:8000/docs -> Swagger UI interactivo (probar endpoints sin Postman)
#    - http://127.0.0.1:8000/redoc -> Documentación alternativa Redoc
# =====================================================================

if __name__ == "__main__":
    # Permite ejecutar el archivo directamente con `python 06_hello_fastapi_setup.py`
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)