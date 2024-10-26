from config.settings import metadata, engine, database
from sqlalchemy import Table
from fastapi import APIRouter
from typing import List
from .schema import Product
from fastapi import HTTPException, status


product_route = APIRouter()
products = Table('products', metadata, autoload_with=engine)


@product_route.get("/products", response_model=List[Product], status_code=200)
async def list_products():

    query = products.select()
    all_products = await database.fetch_all(query)
    if Product is None:
        raise HTTPException(status_code=404, detail="No Product found!")
    else:
        return all_products


@product_route.get("/product/{id}", response_model=Product, status_code=200)
async def retrieve_product(id:int):

    query = products.select().where(products.c.id == id)
    product = await database.fetch_one(query=query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@product_route.post("/product/create/", response_model=Product, status_code=201)
async def create(product: Product):
    query = products.insert().values(name=product.name, description=product.description, price=product.price,
                                    quantity=product.quantity,created=product.created, modified=product.modified)
    last_record_id = await database.execute(query=query)
    return {**product.dict(), "id": last_record_id}


@product_route.patch("/product/update/{id}", response_model=Product, status_code=status.HTTP_200_OK)
async def update(id:int, product: Product):

    existing_record = await database.fetch_one(products.select().where(products.c.id == id))
    if existing_record is None:
        raise HTTPException(status_code=404, detail="Product not found")
    update_data = {
        "name": product.name, 
        "description": product.description, 
        "price": product.price,
        "quantity": product.quantity,
        "created": product.created, 
        "modified": product.modified
    }
    update_data = {key: value for key, value in update_data.items() if value is not None}
    query = products.update().where(products.c.id == id).values(**update_data)
    await database.execute(query=query)
    return {**product.dict(), "id": id}

@product_route.delete("/product/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:int):

    existing_record = await database.fetch_one(products.select().where(products.c.id == id))
    if existing_record is None:
        raise HTTPException(status_code=404, detail="Product not found")
    query = products.delete().where(products.c.id == id)
    await database.execute(query=query)
    return {"message": "Record deleted successfully"}

