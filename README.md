# Sales Insights Backend

Minimal FastAPI backend that turns raw sales records into handy summaries for dashboards and analysts. Built to match the PRD for Avan's Semester 3 project.

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure database** (create `.env` from `.env.example`):
   ```bash
   Copy-Item .env.example .env
   # Edit .env and add your database URL
   ```

3. **Test database connection:**
   ```bash
   python scripts/test_db_connection.py
   ```

4. **Start the server:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Seed sample data** (optional):
   ```bash
   python scripts/seed.py
   ```

## 📁 Project Structure

```
Bussiness Analyst Backend/
├── app/                    # Main application code
│   ├── main.py            # FastAPI app and routes
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # Database operations
│   ├── analytics.py       # Analytics functions
│   └── database.py        # Database configuration
├── scripts/                # Utility scripts
│   ├── seed.py            # Seed sample data
│   ├── test_db_connection.py  # Test database connection
│   └── verify_seed.py     # Verify seeded data
├── tests/                  # Test files
├── docs/                   # Documentation
│   ├── QUICK_START.md     # Quick start guide
│   ├── SETUP_GUIDE.md     # Detailed setup guide
│   └── TROUBLESHOOTING_DB.md  # Database troubleshooting
├── postman/                # API testing
│   └── Sales_Insights_API.postman_collection.json
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## ✨ Features

- SQLAlchemy models with relationships for products, customers, orders, and order items
- CRUD endpoints plus health check
- Analytics endpoints powered by pandas for:
  - Sales over time (daily/weekly/monthly)
  - Top-selling products
  - Category-level summaries
- Optional CSV export for downstream tools
- Tests using pytest and FastAPI's TestClient

## 📚 Documentation

- **[Quick Start Guide](docs/QUICK_START.md)** - Get up and running in 5 minutes
- **[Setup Guide](docs/SETUP_GUIDE.md)** - Detailed setup instructions
- **[Database Troubleshooting](docs/TROUBLESHOOTING_DB.md)** - Fix connection issues

## 🔌 API Endpoints

- `GET /health` – Health check
- `POST /products`, `GET /products` – Product management
- `POST /customers`, `GET /customers` – Customer management
- `POST /orders`, `GET /orders` – Order management
- `GET /analytics/sales-over-time?interval=monthly` – Sales analytics
- `GET /analytics/top-products?limit=5` – Top products
- `GET /analytics/category-summary` – Category summary
- `GET /analytics/sales-export` – CSV export

**API Documentation:**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Test database connection
python scripts/test_db_connection.py
```

## 📦 Postman Collection

Import the Postman collection from `postman/Sales_Insights_API.postman_collection.json` to test all endpoints.

## 🔧 Configuration

The default database is `sqlite:///./sales.db`. Set `DATABASE_URL` in `.env` to point at PostgreSQL (e.g., `postgresql+psycopg2://user:pass@host/db`) for deployment.

## 📝 License

This project is part of Avan's Semester 3 project.

