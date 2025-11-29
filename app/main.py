from datetime import datetime
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Response
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from . import analytics, crud, models, schemas
from .database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sales Insights Backend", version="1.0.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/products", response_model=schemas.ProductRead, status_code=201)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


@app.get("/products", response_model=List[schemas.ProductRead])
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@app.post("/customers", response_model=schemas.CustomerRead, status_code=201)
def add_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)


@app.get("/customers", response_model=List[schemas.CustomerRead])
def list_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)


@app.post("/orders", response_model=schemas.OrderRead, status_code=201)
def add_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_order(db, order)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/orders", response_model=List[schemas.OrderRead])
def list_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)


@app.get("/analytics/sales-over-time", response_model=List[schemas.SalesPoint])
def read_sales_over_time(
    interval: str = "monthly",
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
):
    return analytics.sales_over_time(db, interval, start_date, end_date)


@app.get("/analytics/top-products", response_model=List[schemas.TopProduct])
def read_top_products(
    limit: int = 5,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
):
    clean_limit = min(max(limit, 1), 50)
    return analytics.top_products(db, clean_limit, start_date, end_date)


@app.get("/analytics/category-summary", response_model=List[schemas.CategorySummary])
def read_category_summary(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
):
    return analytics.category_summary(db, start_date, end_date)


@app.get("/analytics/sales-export")
def export_sales(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
):
    csv_content = analytics.sales_csv(db, start_date, end_date)
    if not csv_content:
        return Response(status_code=204)
    return StreamingResponse(
        iter([csv_content]),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=sales_export.csv"},
    )

