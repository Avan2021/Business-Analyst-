from datetime import datetime
from io import StringIO
from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models

try:
    import pandas as pd
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("pandas is required for analytics features.") from exc


def _fetch_sales_rows(
    db: Session, start_date: Optional[datetime], end_date: Optional[datetime]
) -> pd.DataFrame:
    query = (
        db.query(
            models.Order.order_date.label("order_date"),
            models.OrderItem.quantity.label("quantity"),
            models.OrderItem.unit_price.label("unit_price"),
            models.Product.id.label("product_id"),
            models.Product.name.label("product_name"),
            models.Product.category.label("category"),
        )
        .join(models.OrderItem, models.Order.id == models.OrderItem.order_id)
        .join(models.Product, models.Product.id == models.OrderItem.product_id)
    )

    if start_date:
        query = query.filter(models.Order.order_date >= start_date)
    if end_date:
        query = query.filter(models.Order.order_date <= end_date)

    rows = query.all()
    if not rows:
        return pd.DataFrame(
            columns=[
                "order_date",
                "quantity",
                "unit_price",
                "product_id",
                "product_name",
                "category",
            ]
        )

    df = pd.DataFrame(rows, columns=rows[0].keys())
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df


def sales_over_time(
    db: Session, interval: str, start_date: Optional[datetime], end_date: Optional[datetime]
) -> List[dict]:
    freq_map = {"daily": "D", "weekly": "W", "monthly": "M"}
    if interval not in freq_map:
        raise HTTPException(status_code=400, detail="Interval must be daily, weekly, or monthly.")

    df = _fetch_sales_rows(db, start_date, end_date)
    if df.empty:
        return []

    grouped = (
        df.set_index("order_date")
        .groupby(pd.Grouper(freq=freq_map[interval]))
        .agg({"revenue": "sum"})
        .reset_index()
    )
    grouped["revenue"] = grouped["revenue"].round(2)
    return [
        {"period_start": row.order_date.to_pydatetime(), "revenue": float(row.revenue)}
        for row in grouped.itertuples()
    ]


def top_products(
    db: Session, limit: int, start_date: Optional[datetime], end_date: Optional[datetime]
) -> List[dict]:
    df = _fetch_sales_rows(db, start_date, end_date)
    if df.empty:
        return []

    grouped = (
        df.groupby(["product_id", "product_name", "category"])
        .agg({"revenue": "sum", "quantity": "sum"})
        .reset_index()
        .sort_values(by="revenue", ascending=False)
        .head(limit)
    )
    grouped["revenue"] = grouped["revenue"].round(2)
    return grouped.to_dict(orient="records")


def category_summary(
    db: Session, start_date: Optional[datetime], end_date: Optional[datetime]
) -> List[dict]:
    df = _fetch_sales_rows(db, start_date, end_date)
    if df.empty:
        return []

    grouped = df.groupby("category").agg({"revenue": "sum", "quantity": "sum"}).reset_index()
    grouped["revenue"] = grouped["revenue"].round(2)
    return grouped.to_dict(orient="records")


def sales_csv(
    db: Session, start_date: Optional[datetime], end_date: Optional[datetime]
) -> str:
    df = _fetch_sales_rows(db, start_date, end_date)
    if df.empty:
        return ""

    buffer = StringIO()
    export_columns = [
        "order_date",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "revenue",
    ]
    df[export_columns].to_csv(buffer, index=False)
    return buffer.getvalue()

