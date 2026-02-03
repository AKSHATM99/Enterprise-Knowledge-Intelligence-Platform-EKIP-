from fastapi import FastAPI
from api.core.config import settings
from api.api.routes.health import router as health_router
from api.api.routes.query import router as query_router

app = FastAPI(title=settings.app_name)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(query_router, prefix="/query", tags=["query"])
