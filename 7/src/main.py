from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Product(BaseModel):
    name: str = Field(..., title="Название продукта")
    price: float = Field(..., gt=0, title="Цена продукта (больше 0)")
    quantity: int = Field(..., ge=0, title="Количество (>=0)")

class ProductWithID(Product):
    id: int

@app.post("/product")
def add_product(product: Product):
    global product_id_counter
    product_data = product.model_dump()
    product_data['id'] = product_id_counter
    product_list.append(product_data)
    product_id_counter += 1
    return {"message": "Product added successfully", "product": product_data}

@app.get("/products")
def get_products():
    return {"products": product_list}
# END
