from fastapi import FastAPI
from routes import user_routes, book_routes
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

models.Base.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(book_routes.router, prefix="/books", tags=["Books"])
