# Capacitación DevOps
Ejercicios de pruebas para afianzar conocimientos en DevOps.

## API dentro de un contenedor de Docker

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

**Nota**: para verificar el funcionamiento correcto del .dockerignore, se pueden ver los archivos dentro del contenedor desde una terminal (luego de realizar los pasos **1** y **2**). Para ejecutar una terminal dentro del contenedor:
```
docker exec -it <id_contenedor> bash
```
donde el ID del contenedor se puede ver ejecutando el comando:
```
docker ps -a
```

## Integración de MongoDB

Ejercicio de creación de una red de MongoDB e integración al API. Para crear la red, ejecutar:
```
docker network create mongodb-net
```
y para correr el contenedor de MongoDB:
```
docker run -d --name mongodb --network mongodb-net -p 27017:27017 mongo:8.0.0-rc19-noble
```
donde `-d` ejecuta el contenedor en segundo plano, `--name mongodb` le da un nombre al contenedor, y `--network mongodb-net` asocia el contenedor a la red creada.

Ahora, para correr el API podemos seguir implementando el paso **1**, pero debemos introducir un cambio a la hora de correr el contenedor (paso **2**):
```
docker run -d --name python-api --network mongodb-net -p 8000:8000 python-api:latest
```
de esta manera conectaremos a este la red de mongo creada. Para probar el nuevo endpoint podremos ejecutar desde la terminal:
```
curl -g -X GET "http://localhost:8000/guardar-lista-no-ordenada?lista-no-ordenada=[5,4,7,2,7,2]"
```

o ingresar desde el navegador a la URL:  
http://localhost:8000/guardar-lista-no-ordenada?lista-no-ordenada=[5,4,7,2,7,2]
