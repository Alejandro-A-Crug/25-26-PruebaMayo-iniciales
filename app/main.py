from fastapi import FastAPI
from .database import Base, engine
from .routers import items

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(items.router)


# Código que se añade, ALEJANDRO A
@app.get("/status")
def version():
    return {"status": "Alcántara Crugeiras, Alejandro - v.1"}

