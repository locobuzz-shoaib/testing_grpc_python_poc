from typing import Any

from fastapi import FastAPI
from app.api.v1.routers import api_router

from fastapi.responses import JSONResponse
import ujson


class CustomUJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return ujson.dumps(
            content,
            ensure_ascii=False,
            escape_forward_slashes=False
        ).encode("utf-8")


app = FastAPI(deault_response_class=CustomUJSONResponse)

app.include_router(api_router, prefix="/api/v1")
