from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
from pydantic import field_validator

class ProductSpecifications(BaseModel):
    size: str
    color: str
    material: str

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    specifications: ProductSpecifications

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, value):
        if value is None or value <= 0:
            raise ValueError("ensure this value is greater than 0")
        return value

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: float
    specifications: ProductSpecifications

@app.post("/product")
def add_product(product: Product):
    global product_id_counter
    if not product.specifications or not all([
        product.specifications.size,
        product.specifications.color,
        product.specifications.material
    ]):
        raise HTTPException(status_code=400, detail="Invalid product specifications: missing fields")

    product_dict = product.model_dump()
    product_dict["id"] = product_id_counter
    product_list.append(product_dict)
    product_id_counter += 1
    return {
        "id": product_dict["id"],
        "name": product_dict["name"],
        "price": product_dict["price"]
    }

@app.get("/products", response_model=List[ProductResponse])
def get_products():
    return [
        ProductResponse(id=prod["id"], name=prod["name"], price=prod["price"])
        for prod in product_list
    ]

@app.get("/product/{product_id}", response_model=ProductDetailResponse)
def get_product(product_id: int):
    for prod in product_list:
        if prod["id"] == product_id:
            return ProductDetailResponse(
                id=prod["id"],
                name=prod["name"],
                price=prod["price"],
                specifications=ProductSpecifications(**prod["specifications"])
            )
    raise HTTPException(status_code=404, detail="Product not found")

# END