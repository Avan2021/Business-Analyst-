# Project Structure

This document describes the organization of the Sales Insights Backend project.

## 📁 Directory Structure

```
Bussiness Analyst Backend/
│
├── app/                          # Main application package
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # FastAPI application and routes
│   ├── models.py                # SQLAlchemy database models
│   ├── schemas.py               # Pydantic request/response schemas
│   ├── crud.py                  # Database CRUD operations
│   ├── analytics.py             # Analytics and reporting functions
│   └── database.py              # Database configuration and connection
│
├── scripts/                      # Utility and helper scripts
│   ├── seed.py                  # Seed database with sample data
│   ├── test_db_connection.py    # Test database connectivity
│   └── verify_seed.py           # Verify seeded data
│
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py              # Pytest configuration and fixtures
│   └── test_api.py              # API endpoint tests
│
├── docs/                         # Documentation
│   ├── README.md                # Documentation index
│   ├── QUICK_START.md           # Quick start guide
│   ├── SETUP_GUIDE.md           # Detailed setup instructions
│   ├── TROUBLESHOOTING_DB.md    # Database troubleshooting guide
│   ├── FIX_DNS_ERROR.md         # DNS error resolution
│   └── USE_POOLER_CONNECTION.md # Connection pooler guide
│
├── postman/                      # API testing collections
│   └── Sales_Insights_API.postman_collection.json
│
├── .env.example                  # Environment variables template
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── README.md                    # Main project documentation
└── PROJECT_STRUCTURE.md         # This file
```

## 📝 File Descriptions

### Application Code (`app/`)

- **main.py**: FastAPI application entry point, defines all API routes
- **models.py**: SQLAlchemy ORM models (Product, Customer, Order, OrderItem)
- **schemas.py**: Pydantic models for request/response validation
- **crud.py**: Database operations (create, read, update, delete)
- **analytics.py**: Business logic for sales analytics and reporting
- **database.py**: Database engine, session management, connection configuration

### Scripts (`scripts/`)

- **seed.py**: Populates database with sample products, customers, and orders
- **test_db_connection.py**: Diagnostic tool to test database connectivity
- **verify_seed.py**: Verifies that seed data was created successfully

### Tests (`tests/`)

- **conftest.py**: Pytest fixtures and test configuration
- **test_api.py**: Unit and integration tests for API endpoints

### Documentation (`docs/`)

All markdown documentation files are organized here for easy access.

### Postman (`postman/`)

Postman collection JSON file for API testing.

## 🎯 Usage

### Running the Application
```bash
uvicorn app.main:app --reload
```

### Running Scripts
```bash
# Seed database
python scripts/seed.py

# Test database connection
python scripts/test_db_connection.py

# Verify seeded data
python scripts/verify_seed.py
```

### Running Tests
```bash
pytest
```

## 📚 Documentation

See `docs/README.md` for documentation index and guides.

