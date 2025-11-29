# Complete Setup and Testing Guide

## 📋 Prerequisites Checklist

- ✅ Python 3.8+ installed
- ✅ All dependencies installed (`pip install -r requirements.txt`)
- ✅ PostgreSQL database credentials (Supabase)
- ✅ Postman installed

---

## 🚀 Step-by-Step Instructions

### Step 1: Configure Environment Variables

1. **Create your `.env` file** (if not already created):
   ```powershell
   Copy-Item .env.example .env
   ```

2. **Edit `.env` file** and replace `[YOUR_PASSWORD]` with your actual Supabase password:
   ```
   DATABASE_URL=postgresql://postgres:your_actual_password@db.ecjeedhrhotncfvimjxe.supabase.co:5432/postgres
   ```

   **⚠️ CRITICAL: Password URL Encoding**
   
   If your password contains special characters, you **MUST** URL-encode them in the connection string:
   
   **Common special characters that need encoding:**
   - `@` → `%40` (most common issue!)
   - `#` → `%23`
   - `$` → `%24`
   - `%` → `%25`
   - `&` → `%26`
   - `+` → `%2B`
   - `=` → `%3D`
   - `?` → `%3F`
   - `/` → `%2F`
   - `:` → `%3A`
   
   **Example:**
   - If your password is: `mypass@2021`
   - Use in DATABASE_URL: `mypass%402021`
   
   **Quick URL Encoding Tool:**
   - Use online tool: https://www.urlencoder.org/
   - Or Python: `python -c "from urllib.parse import quote; print(quote('your_password'))"`

---

### Step 2: Start the Server

1. **Open a terminal/PowerShell** in the project directory

2. **Start the FastAPI server**:
   ```powershell
   uvicorn app.main:app --reload
   ```

   **Expected Output:**
   ```
   INFO:     Will watch for changes in these directories: ['C:\\Bussiness Analyst Backend']
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process [xxxxx] using WatchFiles
   INFO:     Started server process [xxxxx]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```

3. **Keep this terminal open** - the server must be running to handle API requests

---

### Step 3: Verify PostgreSQL Connection

#### Method 1: Check Server Logs
When the server starts, check the terminal output. If there are no database connection errors, the connection is likely successful.

#### Method 2: Test via Health Endpoint
1. Open your browser and go to: `http://localhost:8000/health`
2. **Expected Response:**
   ```json
   {
     "status": "ok"
   }
   ```

#### Method 3: Check Database Tables (via API)
1. Try creating a product (see Step 4 below)
2. If it succeeds without errors, the database connection is working

#### Method 4: Direct Database Test (Optional)
Create a test script to verify connection:
```powershell
python -c "from app.database import engine; from sqlalchemy import text; conn = engine.connect(); result = conn.execute(text('SELECT version()')); print('PostgreSQL Connected!'); print(result.fetchone()[0]); conn.close()"
```

**Expected Output:**
```
PostgreSQL Connected!
PostgreSQL 15.x on ...
```

**If Connection Fails:**
- Check your `.env` file has the correct password
- Verify your Supabase database is running
- Check if your IP is whitelisted in Supabase (if required)
- Verify the database URL format is correct

---

### Step 4: Import Postman Collection

1. **Open Postman**

2. **Click "Import"** button (top left)

3. **Select the collection file**:
   - Click "Upload Files"
   - Navigate to: `Sales_Insights_API.postman_collection.json`
   - Click "Open"

4. **Verify Import**:
   - You should see "Sales Insights Backend API" collection in the left sidebar
   - It should contain 5 folders:
     - Health Check
     - Products
     - Customers
     - Orders
     - Analytics

5. **Set the Base URL Variable**:
   - Click on the collection name "Sales Insights Backend API"
   - Go to the "Variables" tab
   - Ensure `base_url` is set to: `http://localhost:8000`
   - Click "Save"

---

### Step 5: Test All Endpoints

#### 🟢 1. Health Check
- **Request:** `GET /health`
- **Expected Response (200 OK):**
  ```json
  {
    "status": "ok"
  }
  ```
- **What it means:** Server is running and responding

---

#### 🟢 2. Create Product
- **Request:** `POST /products`
- **Body:**
  ```json
  {
    "name": "Notebook",
    "category": "Stationery",
    "price": 5.0
  }
  ```
- **Expected Response (201 Created):**
  ```json
  {
    "id": 1,
    "name": "Notebook",
    "category": "Stationery",
    "price": 5.0
  }
  ```
- **What it means:** Product successfully created in database

---

#### 🟢 3. List All Products
- **Request:** `GET /products`
- **Expected Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "name": "Notebook",
      "category": "Stationery",
      "price": 5.0
    }
  ]
  ```
- **What it means:** Returns all products in the database

---

#### 🟢 4. Create Customer
- **Request:** `POST /customers`
- **Body:**
  ```json
  {
    "name": "Alice",
    "email": "alice@example.com"
  }
  ```
- **Expected Response (201 Created):**
  ```json
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
  ```
- **What it means:** Customer successfully created

---

#### 🟢 5. List All Customers
- **Request:** `GET /customers`
- **Expected Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "name": "Alice",
      "email": "alice@example.com"
    }
  ]
  ```

---

#### 🟢 6. Create Order
- **Request:** `POST /orders`
- **Body:**
  ```json
  {
    "customer_id": 1,
    "order_date": "2024-01-15T10:30:00",
    "status": "completed",
    "items": [
      {
        "product_id": 1,
        "quantity": 3,
        "unit_price": 5.0
      }
    ]
  }
  ```
- **Expected Response (201 Created):**
  ```json
  {
    "id": 1,
    "customer_id": 1,
    "order_date": "2024-01-15T10:30:00",
    "status": "completed",
    "items": [
      {
        "id": 1,
        "product_id": 1,
        "quantity": 3,
        "unit_price": 5.0
      }
    ]
  }
  ```
- **What it means:** Order created with items
- **Note:** `customer_id` and `product_id` must exist in the database

---

#### 🟢 7. List All Orders
- **Request:** `GET /orders`
- **Expected Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "customer_id": 1,
      "order_date": "2024-01-15T10:30:00",
      "status": "completed",
      "items": [...]
    }
  ]
  ```

---

#### 🟢 8. Sales Over Time (Monthly)
- **Request:** `GET /analytics/sales-over-time?interval=monthly`
- **Expected Response (200 OK):**
  ```json
  [
    {
      "period_start": "2024-01-01T00:00:00",
      "revenue": 150.0
    }
  ]
  ```
- **What it means:** Revenue aggregated by month
- **Intervals available:** `daily`, `weekly`, `monthly`

---

#### 🟢 9. Top Products
- **Request:** `GET /analytics/top-products?limit=5`
- **Expected Response (200 OK):**
  ```json
  [
    {
      "product_id": 1,
      "product_name": "Notebook",
      "category": "Stationery",
      "revenue": 15.0,
      "quantity": 3
    }
  ]
  ```
- **What it means:** Top selling products by revenue
- **Limit range:** 1-50

---

#### 🟢 10. Category Summary
- **Request:** `GET /analytics/category-summary`
- **Expected Response (200 OK):**
  ```json
  [
    {
      "category": "Stationery",
      "revenue": 15.0,
      "quantity": 3
    }
  ]
  ```
- **What it means:** Revenue and quantity grouped by category

---

#### 🟢 11. Sales Export (CSV)
- **Request:** `GET /analytics/sales-export`
- **Expected Response (200 OK):**
  - Content-Type: `text/csv`
  - File download with CSV data
- **What it means:** Downloads a CSV file with all sales data

---

## 📊 Testing Workflow (Recommended Order)

1. ✅ **Health Check** - Verify server is running
2. ✅ **Create Product** - Add at least 2-3 products
3. ✅ **List Products** - Verify products were created
4. ✅ **Create Customer** - Add at least 1-2 customers
5. ✅ **List Customers** - Verify customers were created
6. ✅ **Create Order** - Create orders with items
7. ✅ **List Orders** - Verify orders were created
8. ✅ **Analytics Endpoints** - Test all analytics (should return data if orders exist)

---

## 🔍 Additional Features

### Swagger UI Documentation
- **URL:** `http://localhost:8000/docs`
- Interactive API documentation
- Test endpoints directly from browser
- See request/response schemas

### ReDoc Documentation
- **URL:** `http://localhost:8000/redoc`
- Alternative API documentation format

---

## 🐛 Troubleshooting

### Issue: Server won't start
**Solutions:**
- Check if port 8000 is already in use
- Verify all dependencies are installed
- Check for syntax errors in code

### Issue: Database connection fails
**Solutions:**
- Verify `.env` file exists and has correct `DATABASE_URL`
- Check password encoding (special characters)
- Verify Supabase database is accessible
- Check network/firewall settings

### Issue: 400 Bad Request errors
**Solutions:**
- Verify request body matches the schema
- Check that referenced IDs (customer_id, product_id) exist
- Ensure required fields are provided

### Issue: 500 Internal Server Error
**Solutions:**
- Check server terminal for error messages
- Verify database tables exist (run migrations if needed)
- Check database connection

### Issue: Empty analytics results
**Solutions:**
- Create some orders first
- Verify orders have items
- Check date ranges if using filters

---

## 📝 Quick Reference Commands

```powershell
# Start server
uvicorn app.main:app --reload

# Start server on different port
uvicorn app.main:app --reload --port 8001

# Seed sample data (optional)
python scripts/seed.py

# Run tests
pytest

# Run tests with verbose output
pytest -v
```

---

## ✅ Success Checklist

- [ ] Server starts without errors
- [ ] Health check returns `{"status": "ok"}`
- [ ] Can create products successfully
- [ ] Can create customers successfully
- [ ] Can create orders successfully
- [ ] Analytics endpoints return data
- [ ] Postman collection imported and working
- [ ] All endpoints tested and returning expected responses

---

## 🎯 Next Steps

1. **Seed Sample Data** (optional):
   ```powershell
   python scripts/seed.py
   ```
   This will populate your database with sample products, customers, and orders for testing analytics.

2. **Explore Swagger UI**: Visit `http://localhost:8000/docs` for interactive API testing

3. **Build Your Frontend**: Use these APIs to build your dashboard/analytics frontend

---

## 📞 Need Help?

- Check server terminal for error messages
- Review FastAPI documentation: https://fastapi.tiangolo.com/
- Check SQLAlchemy documentation: https://docs.sqlalchemy.org/
- Review Postman collection for example requests

