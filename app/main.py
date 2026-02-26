from fastapi import FastAPI, HTTPException

from app.service.products import get_allProducts

app = FastAPI()

@app.get("/")
def root():
    return {"message" :"hello api"}


@app.get("/products")
def get_Product():

    return get_allProducts()
  
