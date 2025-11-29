from datetime import datetime

import pytest


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_product_and_list(client):
    payload = {"name": "Marker", "category": "Stationery", "price": 2.5}
    create_response = client.post("/products", json=payload)
    assert create_response.status_code == 201

    list_response = client.get("/products")
    data = list_response.json()
    assert any(product["name"] == "Marker" for product in data)


def test_create_customer_and_order(client):
    customer = client.post("/customers", json={"name": "Carol", "email": "carol@example.com"}).json()
    product = client.post("/products", json={"name": "Stapler", "category": "Office", "price": 8}).json()

    order_payload = {
        "customer_id": customer["id"],
        "order_date": datetime.utcnow().isoformat(),
        "status": "completed",
        "items": [
            {"product_id": product["id"], "quantity": 2},
        ],
    }
    response = client.post("/orders", json=order_payload)
    assert response.status_code == 201
    assert response.json()["items"][0]["quantity"] == 2


def test_sales_over_time(seeded_client):
    response = seeded_client.get("/analytics/sales-over-time", params={"interval": "weekly"})
    assert response.status_code == 200
    body = response.json()
    assert len(body) >= 2
    assert all("revenue" in row for row in body)


def test_top_products_limit(seeded_client):
    response = seeded_client.get("/analytics/top-products", params={"limit": 1})
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_category_summary(seeded_client):
    response = seeded_client.get("/analytics/category-summary")
    assert response.status_code == 200
    categories = {row["category"] for row in response.json()}
    assert "Stationery" in categories
    assert "Electronics" in categories


def test_invalid_interval_error(seeded_client):
    response = seeded_client.get("/analytics/sales-over-time", params={"interval": "yearly"})
    assert response.status_code == 400

