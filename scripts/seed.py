import random
from datetime import datetime, timedelta

from app import crud, schemas
from app.database import db_session

random.seed(7)


def run():
    with db_session() as db:
        db.execute("DELETE FROM order_items")
        db.execute("DELETE FROM orders")
        db.execute("DELETE FROM products")
        db.execute("DELETE FROM customers")

        products = [
            schemas.ProductCreate(name="Notebook", category="Stationery", price=5.0),
            schemas.ProductCreate(name="Pen Set", category="Stationery", price=12.0),
            schemas.ProductCreate(name="Desk Lamp", category="Electronics", price=45.0),
            schemas.ProductCreate(name="Office Chair", category="Furniture", price=120.0),
        ]
        product_rows = [crud.create_product(db, product) for product in products]

        customers = [
            schemas.CustomerCreate(name="Alice", email="alice@example.com"),
            schemas.CustomerCreate(name="Bob", email="bob@example.com"),
        ]
        customer_rows = [crud.create_customer(db, customer) for customer in customers]

        base_date = datetime.utcnow() - timedelta(days=30)
        for offset in range(12):
            order_items = []
            for _ in range(2):
                product = random.choice(product_rows)
                order_items.append(
                    schemas.OrderItemCreate(
                        product_id=product.id,
                        quantity=random.randint(1, 4),
                        unit_price=product.price,
                    )
                )
            order = schemas.OrderCreate(
                customer_id=random.choice(customer_rows).id,
                order_date=base_date + timedelta(days=offset * 2),
                status="completed",
                items=order_items,
            )
            crud.create_order(db, order)

    print("Database seeded with sample data.")


if __name__ == "__main__":
    run()

