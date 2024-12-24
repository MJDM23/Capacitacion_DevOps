import os
import time
import logging
import requests


log_file = '/opt/monitor/logs/api-monitor.log'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

target_host = os.getenv('TARGET_CONTAINER_HOST', 'localhost')
target_port = os.getenv('TARGET_CONTAINER_PORT', '8000')
check_interval = int(os.getenv('CHECK_INTERVAL', 5))


def monitor():
    """Función que realiza solicitudes periódicas a un endpoint de healthcheck para
    verificar el estado del contenedor.

    Ejemplo de logs generados:
        .. code-block:: python

            2024-09-26 12:30:00,123 - INFO - Se hizo la solicitud al endpoint http://api-container:8000/healthcheck y devolvió OK
            2024-09-26 12:30:05,456 - ERROR - Se hizo la solicitud al endpoint http://api-container:8000/healthcheck y devolvió error: Código de estado: 500, Respuesta: Internal Server Error

    # noqa
    """
    url = f'http://{target_host}:{target_port}/healthcheck'
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200 and response.text.strip() == 'OK':
                logging.info(f'Se hizo la solicitud al endpoint {url} y devolvió OK')
            else:
                logging.error(
                    f'Se hizo la solicitud al endpoint {url} y devolvió error: Código de '
                    f'estado: {response.status_code}, Respuesta: {response.text}'
                )
        except Exception as error:
            logging.error(f'Error al intentar acceder al endpoint {url}: {error}')
        time.sleep(check_interval)


if __name__ == "__main__":
    monitor()
