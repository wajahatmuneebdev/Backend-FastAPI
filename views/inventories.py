from fastapi import APIRouter, Depends
from data_access_layer.db import get_db
from business_layer.inventories import (
    fetch_inventory,
    update_inventory,
    get_inventory_changes,
)

router = APIRouter()


@router.get("/inventory/{product_id}")
async def get(product_id, db_session=Depends(get_db)):
    return fetch_inventory(db_session, product_id)


@router.put("/inventory/{product_id}/update")
async def put(product_id, quantity_change, db_session=Depends(get_db)):
    update_inventory(db_session, product_id, int(quantity_change))

    return {"message": "Inventory updated successfully"}


@router.get("/inventory/{product_id}/changes")
async def get(
    product_id,
    db_session=Depends(get_db),
):
    return {"inventory_changes": get_inventory_changes(db_session, product_id)}
