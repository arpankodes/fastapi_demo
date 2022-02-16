
# fastAPI Setup



## Installation

Install fastapi and uvicorn

```bash
  pip install fastapi
  pip install "uvicorn[standard]"
```
    
## Create

create a file main.py in the project directory with:
```bash
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
```
    
## Runserver

runserver by executing:

```bash
uvicorn main:app --reload
```
## Interactive API doc (swagger)

Check the link below to see the automatic interactive API doc

http://127.0.0.1:8000/docs