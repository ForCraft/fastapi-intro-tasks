from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
from pydantic import BaseModel, Field, field_validator

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
    def price_must_be_positive(cls, v):
        if v is None or v <= 0:
            raise ValueError("ensure this value is greater than 0")
        return v

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
    return {"message": "Product added successfully", "product": product_dict}

@app.get("/products")
def get_products():
    return {"products": product_list}

# END
