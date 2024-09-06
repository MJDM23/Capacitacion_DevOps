# External libraries
import os
from functools import lru_cache
from pymongo import MongoClient
from pymongo.database import Database


@lru_cache()
def get_mongo_db() -> Database:
    """Crea un cliente de MongoDB y devuelve la base de datos 'python_app'.

    Returns:
        Base de datos 'python_app'.

    """
    mongo_host = os.environ.get('MONGODB_HOST')
    mongo_port = os.environ.get('MONGODB_PORT')

    client = MongoClient(mongo_host, int(mongo_port))

    mongo_db = client.python_app

    return mongo_db
