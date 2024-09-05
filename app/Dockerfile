FROM python:3.12.5-slim

# deshabilitar la escritura de archivos de bytecode (__pycache__)
# para verificar funcionamiento correcto de .dockerignore:
# ENV PYTHONDONTWRITEBYTECODE=1

COPY . /opt/python-api/

WORKDIR /opt/python-api/

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
