from fastapi import FastAPI
from app.routers import products

app = FastAPI()

app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Bienvenido a PriceSpy 🚀"}