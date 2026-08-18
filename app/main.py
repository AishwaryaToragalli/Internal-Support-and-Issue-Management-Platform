from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base
from app.database import engine
from app.routers import tickets


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Internal Support Platform",
    description="Internal technical issue management API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(tickets.router)


@app.get("/")
def home():
    return {
        "message": "Internal Support Platform is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
