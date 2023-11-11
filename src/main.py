from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import routers
from lib import settings, database, sentry
from lib.exceptions import exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI):
    sentry.configure()
    await database.startup()
    yield


app = FastAPI(
    debug=settings.app.DEBUG,
    exception_handlers=exception_handlers(),
    lifespan=lifespan,
)

for router in routers:
    app.include_router(router, prefix="/api")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", tags=["Default"])
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", context={"request": request})
