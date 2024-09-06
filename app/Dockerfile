FROM python:3.12.5-slim

# deshabilitar la escritura de archivos de bytecode (__pycache__)
# para verificar funcionamiento correcto de .dockerignore:
# ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /opt/python-api/

COPY . .

RUN pip install -r requirements.txt

ENV MONGODB_HOST=mongodb
ENV MONGODB_PORT=27017

ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
