from pydantic import BaseSettings
from pymongo import mongo_client
import pymongo


class Settings(BaseSettings):
    MONGO_URL: str
    MONGO_INITDB_DATABASE: str

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str

    CLIENT_ORIGIN: str

    class Config:
        env_file = '.env'


settings = Settings()

client = mongo_client.MongoClient(settings.MONGO_URL, serverSelectionTimeoutMS=5000)

try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception:
    print('Unable to connect to the MongoDB server.')

db = client[settings.MONGO_INITDB_DATABASE]
