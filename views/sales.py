from fastapi import APIRouter, Depends
from business_layer.sales import fetch_sales, fetch_revenue
from data_access_layer.db import get_db

router = APIRouter()


@router.get("/sales")
async def get(filters=[], db_session=Depends(get_db)):
    return fetch_sales(db_session, filters)


@router.get("/revenue")
async def get(
    period,
    category_name=None,
    start_date=None,
    end_date=None,
    db_session=Depends(get_db),
):
    return {
        "revenue": fetch_revenue(
            db_session, period, category_name, start_date, end_date
        )
    }
