from data_access_layer.utils import apply_filters
from data_access_layer.models.sale import Sale
from data_access_layer.models.product import Product
from data_access_layer.models.category import Category
from sqlalchemy import func, extract


def fetch_sales(db_session, filters):
    query = apply_filters(db_session, Sale, filters)

    return query.all()


def fetch_revenue(db_session, period, category_name, start_date, end_date):
    if period not in ["daily", "weekly", "monthly", "annual", "date_range"]:
        return {"error": "Invalid period"}

    query = db_session.query(
        func.date(Sale.sale_date).label("date"),
        func.sum(Sale.quantity * Product.price).label("revenue"),
    )

    if category_name:
        query = (
            query.join(Sale.product)
            .join(Product.category)
            .filter(Category.name == category_name)
        )

    if period == "daily":
        query = query.group_by(func.date(Sale.sale_date))
        query = query.with_entities(
            func.date(Sale.sale_date).label("date"),
            func.sum(Sale.quantity * Product.price).label("revenue"),
        )
        query = query.order_by(func.date(Sale.sale_date).desc())

    elif period == "weekly":
        query = query.group_by(func.date_trunc("week", Sale.sale_date))
        query = query.with_entities(
            func.date_trunc("week", Sale.sale_date).label("week"),
            func.sum(Sale.quantity * Product.price).label("revenue"),
        )
        query = query.order_by(func.date_trunc("week", Sale.sale_date).desc())

    elif period == "monthly":
        query = query.group_by(func.date_trunc("month", Sale.sale_date))
        query = query.with_entities(
            func.date_trunc("month", Sale.sale_date).label("month"),
            func.sum(Sale.quantity * Product.price).label("revenue"),
        )
        query = query.order_by(func.date_trunc("month", Sale.sale_date).desc())

    elif period == "annual":
        query = query.group_by(func.date_trunc("year", Sale.sale_date))
        query = query.with_entities(
            func.date_trunc("year", Sale.sale_date).label("year"),
            func.sum(Sale.quantity * Product.price).label("revenue"),
        )
        query = query.order_by(func.date_trunc("year", Sale.sale_date).desc())

    elif period == "date_range":
        if not start_date or not end_date:
            return {
                "error": "Both start_date and end_date are required for date_range period"
            }

        query = query.filter(
            Sale.sale_date >= start_date, Sale.sale_date <= end_date
        ).group_by(func.date(Sale.sale_date))

    return query.all()
