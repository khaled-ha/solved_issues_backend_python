from connections.env_var_db_config import EnvVars
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from logging import getLogger

logger = getLogger(__name__)


def get_db_session():
    engine = create_engine(EnvVars().database_session_url)
    connection = engine.connect()
    try:
        return sessionmaker(bind=connection)
    except SQLAlchemyError as e:
        logger.warn(e)
    except Exception as e:
        logger.debug(e)
