"""Quick script to verify seeded data"""
from app.database import db_session
from app.models import Product, Customer, Order
from sqlalchemy import func

with db_session() as db:
    products_count = db.query(func.count(Product.id)).scalar()
    customers_count = db.query(func.count(Customer.id)).scalar()
    orders_count = db.query(func.count(Order.id)).scalar()
    
    print("=" * 50)
    print("Database Seeding Verification")
    print("=" * 50)
    print(f"✅ Products: {products_count}")
    print(f"✅ Customers: {customers_count}")
    print(f"✅ Orders: {orders_count}")
    print("=" * 50)
    
    if products_count > 0 and customers_count > 0 and orders_count > 0:
        print("✅ Database successfully seeded!")
    else:
        print("⚠️  Some tables are empty. Run seed script again.")

