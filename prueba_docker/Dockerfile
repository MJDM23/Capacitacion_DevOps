FROM python:3.12.5-slim

COPY main.py /opt/python-api/

WORKDIR /opt/python-api/

COPY requirements.txt /opt/python-api/
RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
