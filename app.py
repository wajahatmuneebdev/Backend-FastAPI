from fastapi import FastAPI
from views.root import router as default_router
from views.sales import router as sales_router
from views.inventories import router as inventories_router
from views.products import router as products_router
from data_access_layer.db import init_db
from data_access_layer.seed import create_schema
from data_access_layer.demo_data import load_demo_data

app = FastAPI()

init_db()

create_schema()

load_demo_data()

app.include_router(default_router)
app.include_router(sales_router)
app.include_router(inventories_router)
app.include_router(products_router)
