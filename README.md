# E-commerce Admin Dashboard API

This is an API for an E-commerce Admin Dashboard, designed to provide detailed insights into sales, revenue, inventory status, and product management. It is built using Python, FastAPI, SQLAlchemy, and PostgreSQL.

## Features

- Sales Status:
  - Retrieve, filter, and analyze sales data.
  - Analyze revenue on a daily, weekly, monthly, and annual basis.
  - Compare revenue across different periods and categories.
  - Provide sales data by date range, product, and category.

- Inventory Management:
  - View current inventory status, including low stock alerts.
  - Update inventory levels and track changes over time.
  - Register new products.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- PostgreSQL database

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/wajahatmuneebdev/Backend-FastAPI.git
   cd Backend-FastAPI

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt

6. Configure the database connection in data_access_layer/db.py:

   ```bash
   DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"

## Usage

- Start the API server:

  ```bash
  uvicorn main:app --host localhost --port 8000 --reload

### API Endpoints

- Sales: **`/sales`**
- Revenue Analysis: **`/revenue`**
- Inventory: **`/inventory`**
- Low Stock Alerts: **`/inventory/low-stock-alerts`**
- Update Inventory: **`/inventory/update`**
- Register New Product: **`/products/register`**
