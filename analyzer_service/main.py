from contextlib import asynccontextmanager

from fastapi import FastAPI

from analyzer_service.presentation.api.dependencies import Container
from analyzer_service.presentation.api.exceptions import register_exception_handlers
from analyzer_service.presentation.api.router import build_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.container = Container()
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="Document Analyzer API", lifespan=lifespan)
    register_exception_handlers(app)

    @app.get("/health", status_code=200)
    def health() -> dict[str, str]:
        return {"detail": "ok"}

    app.include_router(build_router())
    return app


app = create_app()
