# 🚀 Quick Start Guide

## ⚡ 5-Minute Setup

### 1️⃣ Configure Database
```powershell
# Copy example file
Copy-Item .env.example .env

# Edit .env and add your Supabase password
# DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@db.ecjeedhrhotncfvimjxe.supabase.co:5432/postgres
```

### 2️⃣ Test Database Connection
```powershell
python test_db_connection.py
```
**Expected:** ✅ Connection successful message

### 3️⃣ Start Server
```powershell
uvicorn app.main:app --reload
```
**Expected:** Server running on http://127.0.0.1:8000

### 4️⃣ Verify Server
- Open browser: http://localhost:8000/health
- Should see: `{"status": "ok"}`

### 5️⃣ Import Postman Collection
1. Open Postman
2. Click "Import"
3. Select `Sales_Insights_API.postman_collection.json`
4. Collection appears in sidebar
5. Test "Health Check" endpoint

---

## 📋 Testing Checklist

Run these in Postman (in order):

- [ ] **Health Check** → Should return `{"status": "ok"}`
- [ ] **Create Product** → Should return product with ID
- [ ] **List Products** → Should show created products
- [ ] **Create Customer** → Should return customer with ID
- [ ] **Create Order** → Should return order with items
- [ ] **Sales Over Time** → Should return revenue data
- [ ] **Top Products** → Should return top selling products

---

## 🎯 Expected Outcomes Summary

| Endpoint | Method | Status | Response |
|----------|--------|--------|----------|
| `/health` | GET | 200 | `{"status": "ok"}` |
| `/products` | POST | 201 | Product object with ID |
| `/products` | GET | 200 | Array of products |
| `/customers` | POST | 201 | Customer object with ID |
| `/customers` | GET | 200 | Array of customers |
| `/orders` | POST | 201 | Order object with items |
| `/orders` | GET | 200 | Array of orders |
| `/analytics/sales-over-time` | GET | 200 | Array of sales points |
| `/analytics/top-products` | GET | 200 | Array of top products |
| `/analytics/category-summary` | GET | 200 | Array of category summaries |
| `/analytics/sales-export` | GET | 200 | CSV file download |

---

## 🔗 Useful URLs

- **API Server:** http://localhost:8000
- **Health Check:** http://localhost:8000/health
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## ⚠️ Common Issues

**Problem:** Database connection fails
- ✅ Check `.env` file exists and has correct password
- ✅ Run `python test_db_connection.py` to diagnose

**Problem:** Port 8000 already in use
- ✅ Use different port: `uvicorn app.main:app --reload --port 8001`
- ✅ Update Postman `base_url` variable

**Problem:** Empty analytics results
- ✅ Create some orders first
- ✅ Run `python scripts/seed.py` for sample data

---

## 📚 Full Documentation

See `SETUP_GUIDE.md` for complete detailed instructions.

