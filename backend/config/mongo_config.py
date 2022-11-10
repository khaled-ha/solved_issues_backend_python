from pydantic import BaseSettings
from pymongo import MongoClient
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
        env_file = '../../.env'


settings = Settings()
client = MongoClient(
    'mongodb://solved_issue_user:solved_issues_password@mongo:27017/solved_issues?authSource=admin',
    serverSelectionTimeoutMS=5000,
)

try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception as e:
    print(e)
    print('Unable to connect to the MongoDB server.')

db = client[settings.MONGO_INITDB_DATABASE]
User = db.users
Post = db.get_collection('posts')
# User.create_index([("email", pymongo.ASCENDING)], unique=True)
# Post.create_index([('title', pymongo.ASCENDING)], unique=True)
