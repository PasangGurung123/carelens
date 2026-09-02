from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered healthcare analytics platform API",
)


app.include_router(
    router,
    prefix="/api/v1",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CareLens API",
        "version": settings.app_version,
    }