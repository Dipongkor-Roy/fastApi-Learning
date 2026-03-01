from fastapi import FastAPI, HTTPException, Query  # query for query parameters

from app.service.products import get_allProducts

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello api"}


# @app.get("/products")
# def get_Product():

#     return get_allProducts()


@app.get("/products")
def list_products(
    name: str = Query(
        default=None, min_length=1, max_length=50, description="Search by products name"
    ),
):

    products = get_allProducts()
    if name:
        niddle = name.strip().lower()
        products = [p for p in products if niddle in p.get("name", "").lower()]
        if not products:
            raise HTTPException(
                status_code=404, detail="No products found with the given name={name}"
            )

        total = len(products)

    return {"total": total, "products": products}
