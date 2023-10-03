from fastapi import APIRouter, Depends
from data_access_layer.db import get_db
from business_layer.products import register_new_product

router = APIRouter()


@router.post("/products/register")
async def post(product_data, db_session=Depends(get_db)):
    register_new_product(db_session, product_data)

    return {"message": "New product registered successfully"}
