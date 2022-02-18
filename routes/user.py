from fastapi import APIRouter
from config.db import conn
from models.index import user
from schemas.index import user

user = APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(user.select()).fetchall()

@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(user.select()).fetchall()

@user.post("/")
async def write_data():
    conn.execute(user.insert().values(
         name=user.name,
    ))
    return conn.execute(user.select()).fetchall()
       
    
