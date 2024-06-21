from fastapi import APIRouter
from app.api.v1.endpoints import hello

api_router = APIRouter()
api_router.include_router(hello.router, prefix="/hello", tags=["hello"])
