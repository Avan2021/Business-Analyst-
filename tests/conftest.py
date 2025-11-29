from datetime import datetime, timedelta

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import crud, schemas
from app.database import Base, get_db
from app.main import app

TEST_DB_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def create_tables():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(db_session):
    def _override():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _override
    return TestClient(app)


def seed_sample_data(db):
    products = [
        crud.create_product(db, schemas.ProductCreate(name="Notebook", category="Stationery", price=5)),
        crud.create_product(db, schemas.ProductCreate(name="Desk Lamp", category="Electronics", price=40)),
    ]
    customers = [
        crud.create_customer(db, schemas.CustomerCreate(name="Alice", email="alice@example.com")),
        crud.create_customer(db, schemas.CustomerCreate(name="Bob", email="bob@example.com")),
    ]
    base_date = datetime(2024, 1, 1)

    order_one = schemas.OrderCreate(
        customer_id=customers[0].id,
        order_date=base_date,
        status="completed",
        items=[
            schemas.OrderItemCreate(product_id=products[0].id, quantity=3, unit_price=5),
            schemas.OrderItemCreate(product_id=products[1].id, quantity=1, unit_price=40),
        ],
    )
    order_two = schemas.OrderCreate(
        customer_id=customers[1].id,
        order_date=base_date + timedelta(days=7),
        status="completed",
        items=[schemas.OrderItemCreate(product_id=products[1].id, quantity=2, unit_price=40)],
    )
    crud.create_order(db, order_one)
    crud.create_order(db, order_two)
    return {"products": products, "customers": customers}


@pytest.fixture
def seeded_client(client, db_session):
    seed_sample_data(db_session)
    return client

