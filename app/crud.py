from datetime import datetime
from typing import List

from . import models
from sqlalchemy.orm import Session

from .. import schemas


def create_product(db: Session, product: schemas.ProductCreate) -> models.Product:
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session) -> List[models.Product]:
    return db.query(models.Product).order_by(models.Product.id).all()


def create_customer(db: Session, customer: schemas.CustomerCreate) -> models.Customer:
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def get_customers(db: Session) -> List[models.Customer]:
    return db.query(models.Customer).order_by(models.Customer.id).all()


def create_order(db: Session, order_data: schemas.OrderCreate) -> models.Order:
    db_order = models.Order(
        customer_id=order_data.customer_id,
        order_date=order_data.order_date or datetime.utcnow(),
        status=order_data.status or "created",
    )
    db.add(db_order)
    db.flush()

    for item in order_data.items:
        product = db.get(models.Product, item.product_id)
        if not product:
            raise ValueError(f"Product {item.product_id} not found.")
        unit_price = item.unit_price if item.unit_price is not None else product.price
        db_item = models.OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price=unit_price,
        )
        db.add(db_item)

    db.commit()
    db.refresh(db_order)
    return db_order


def get_orders(db: Session) -> List[models.Order]:
    return db.query(models.Order).order_by(models.Order.order_date.desc()).all()

