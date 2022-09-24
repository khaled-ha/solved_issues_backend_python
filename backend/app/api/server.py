from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router
from app.events import create_start_app_handler, stop_app_handler

def get_application():
    app = FastAPI(title="Solved_issues", version="1.0.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")
    app.add_event_handler('startup', create_start_app_handler(app))
    app.add_event_handler('shutdown', stop_app_handler(app))
    return app

app = get_application()