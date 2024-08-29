from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()

@app.get("/lista-ordenada")
def lista_ordenada(lista_no_ordenada: str = Query(..., alias="lista-no-ordenada")):
    lista_no_ordenada = lista_no_ordenada.strip('[]').split(',')
    lista_no_ordenada = [int(i) for i in lista_no_ordenada]
    lista_ordenada = sorted(lista_no_ordenada)

    hora_sistema = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    respuesta = {
        "hora_sistema": hora_sistema,
        "lista_ordenada": lista_ordenada
    }

    return respuesta

@app.get("/healthcheck")
def healthcheck():
    respuesta = "OK"

    return respuesta
