from sqlalchemy import and_, or_

operator_mapping = {
    "eq": lambda col, val: col == val,
    "neq": lambda col, val: col != val,
    "in": lambda col, val: col.in_(val),
    "nin": lambda col, val: ~col.in_(val),
    "gt": lambda col, val: col > val,
    "lt": lambda col, val: col < val,
    "gte": lambda col, val: col >= val,
    "lte": lambda col, val: col <= val,
    "like": lambda col, val: col.like(val),
    "ilike": lambda col, val: col.ilike(val),
    "not_like": lambda col, val: ~col.like(val),
    "not_ilike": lambda col, val: ~col.ilike(val),
}


def apply_filters(db_session, model, filters):
    """
    Args:
        - db_session (Session): SQLAlchemy database session.
        - model (Base): SQLAlchemy table model.
        - filters (List[dict]): List of filter objects in the extended format.

    Returns:
        SQLAlchemy query with applied filters.
    """
    query = db_session.query(model)

    for filter_obj in filters:
        if "and" in filter_obj:
            and_conditions = apply_filters(db_session, model, filter_obj["and"])
            query = query.filter(and_(*and_conditions))
        elif "or" in filter_obj:
            or_conditions = apply_filters(db_session, model, filter_obj["or"])
            query = query.filter(or_(*or_conditions))
        else:
            column = filter_obj["column"]
            operator = filter_obj["operator"]
            values = filter_obj["values"]

            if operator in operator_mapping:
                condition = operator_mapping[operator](
                    model.__table__.c[column], values
                )
                query = query.filter(condition)

    return query
