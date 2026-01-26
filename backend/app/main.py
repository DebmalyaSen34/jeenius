from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.session import engine, Base
from app.api.routers import auth, tutor

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.project_name, version=settings.project_version)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)  

app.include_router(auth.router)
app.include_router(tutor.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Tutoring Service API!"
    }