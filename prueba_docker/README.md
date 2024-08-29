Ejercicio de creación de un contenedor de Docker con ejecución de una API. Para probar el contenedor, seguir estos pasos:

### 1. Construir la imagen Docker:
Abrir una terminal en el directorio donde se encuentra el Dockerfile y ejecutar el siguiente comando:
```
docker build -t python-api .
```

### 2.Ejecutar el contenedor: 
Una vez la imagen se haya construido correctamente, se puede ejecutar el contenedor con el siguiente comando:
```
docker run -d -p 8000:8000 python-api
```
Este comando ejecutará el contenedor en segundo plano (opción `-d`) y mapeará el puerto 8000 del contenedor al puerto 8000 de tu máquina local.

### 3.Probar los endpoints:
Para probar los endpoints abrir el navegador web y acceder a las siguientes URLs:
http://localhost:8000/lista-ordenada?lista-no-ordenada=[5,4,7,2,7,2]
http://localhost:8000/healthcheck


o ejecutar desde la terminal los siguientes comandos:
```
curl -g -X GET "http://localhost:8000/lista-ordenada?lista-no-ordenada=[5,4,7,2,7,2]"
curl -X GET "http://localhost:8000/healthcheck"
```
la opción `-g` en el primer comando desactiva el globbing (curl interpreta los corchetes [] como caracteres especiales para el globbing de URLs, por lo que si no se desactiva lanzará error la petición)
