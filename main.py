from fastapi import FastAPI
from src.routes.users import router as user_router
from src.routes.auth import router as auth_router

app= FastAPI(title="User Authentication")

app.include_router(user_router) 
app.include_router(auth_router)