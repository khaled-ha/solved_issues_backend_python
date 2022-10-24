from fastapi import FastAPI
from databases import Database
from conf.env_var_db_config import EnvVars
import logging

logger = logging.getLogger(__name__)

async def get_connect_db(app: FastAPI):
    database = Database(EnvVars().database_docker_url, min_size=2, max_size=5)
    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warning("--- DB CONNECTION ERROR ---")
        logger.warning(e)
        logger.warning("--- DB CONNECTION ERROR ---")


async def close_db(app: FastAPI):
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")