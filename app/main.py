# External libraries
import uuid
from fastapi import FastAPI, Query
from datetime import datetime

# Own libraries
from config_mongo import get_mongo_db

app = FastAPI()


@app.get("/guardar-lista-no-ordenada")
def guardar_lista_no_ordenada(
    lista_no_ordenada: str = Query(..., alias="lista-no-ordenada")
) -> dict:
    """Endpoint que recibe una lista no ordenada, la guarda en MongoDB y devuelve un
    mensaje con el ID asignado.

    Args:
        lista_no_ordenada: Lista de números no ordenados en formato string.

    Returns:
        Un diccionario con un mensaje que incluye el ID único generado.

    Examples:
        .. code-block:: python

            {
                "msg": "La lista no ordenada fue guardada con el id: 9743ee94-6690-11ef-a4d5-089df4cb467e"
            }

    #noqa
    """
    lista_no_ordenada = lista_no_ordenada.strip('[]').split(',')
    lista_no_ordenada = [int(i) for i in lista_no_ordenada]

    hora_sistema = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_unico = str(uuid.uuid4())

    datos = {
        "id": id_unico,
        "hora_sistema": hora_sistema,
        "lista_no_ordenada": lista_no_ordenada,
    }

    db = get_mongo_db()
    coleccion = db.listas_no_ordenadas
    coleccion.insert_one(datos)

    respuesta = {"msg": f"La lista no ordenada fue guardada con el id: {id_unico}"}

    return respuesta


@app.get("/healthcheck")
def healthcheck() -> str:
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
def lista_ordenada(
    lista_no_ordenada: str = Query(..., alias="lista-no-ordenada")
) -> dict:
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
