from typing import Callable
from fastapi import FastAPI
from tasks.db_tasks import get_connect_db, close_db


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app():
        await get_connect_db(app)

    return start_app


def stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app():
        await close_db(app)

    return stop_app
