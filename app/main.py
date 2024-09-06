from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    """Endpoint para verificar el estado de salud del servicio.

    Returns:
        Un string que indica el estado de salud del servicio.

    Examples:
        .. code-block:: python

            "OK"

    """
    respuesta = "OK"

    return respuesta


@app.get("/lista-ordenada")
def lista_ordenada(lista_no_ordenada: str = Query(..., alias="lista-no-ordenada")):
    """Endpoint que recibe una lista no ordenada y devuelve la lista ordenada junto
    con la hora del sistema.

    Args:
        lista_no_ordenada: Lista de números no ordenados en formato string.

    Returns:
        Un diccionario con la hora del sistema y la lista ordenada.

    Examples:
        .. code-block:: python

            {
                "hora_sistema": "2024-09-03 21:51:23",
                "lista_ordenada": [1, 2, 3, 3, 6]
            }

    """
    lista_no_ordenada = lista_no_ordenada.strip('[]').split(',')
    lista_no_ordenada = [int(i) for i in lista_no_ordenada]
    lista_ordenada = sorted(lista_no_ordenada)

    hora_sistema = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    respuesta = {"hora_sistema": hora_sistema, "lista_ordenada": lista_ordenada}

    return respuesta
