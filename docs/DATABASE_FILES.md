# Database Files Explanation

## 📁 SQLite Database Files

You may see these SQLite database files in your project root:

- `sales.db` - Default SQLite database (fallback)
- `test.db` - Test database used by pytest

## 🔍 What Are They?

### `sales.db`
- **Purpose**: Default SQLite database file
- **When created**: When the app runs without a `DATABASE_URL` in `.env`, or if `DATABASE_URL` points to SQLite
- **Location**: Project root directory
- **Used by**: Main application (as fallback)

**Code reference** (`app/database.py`):
```python
return os.getenv("DATABASE_URL", "sqlite:///./sales.db")
```

### `test.db`
- **Purpose**: Test database for pytest
- **When created**: When you run `pytest` tests
- **Location**: Project root directory
- **Used by**: Test suite (`tests/conftest.py`)

**Code reference** (`tests/conftest.py`):
```python
TEST_DB_URL = "sqlite:///./test.db"
```

## ✅ Current Status

Since you're using **PostgreSQL (Supabase)**:
- ✅ Your production database is PostgreSQL (Supabase)
- ⚠️ `sales.db` is **not needed** (leftover from earlier testing)
- ⚠️ `test.db` is **automatically created/deleted** by pytest during tests

## 🗑️ Can I Delete Them?

### `sales.db`
**Yes, you can delete it** if:
- ✅ You're using PostgreSQL (Supabase) for production
- ✅ You have `DATABASE_URL` set in your `.env` file
- ✅ You don't need the old SQLite data

**Keep it if:**
- You want to switch back to SQLite for local development
- You need the data stored in it

### `test.db`
**You can delete it**, but:
- It will be **automatically recreated** when you run `pytest`
- It's **automatically cleaned up** after tests complete
- It's safe to delete - tests will recreate it

## 🧹 Clean Up

If you want to remove these files:

```powershell
# Delete sales.db (if not needed)
Remove-Item sales.db

# Delete test.db (will be recreated by tests)
Remove-Item test.db
```

## 📝 Important Notes

1. **Both files are in `.gitignore`** - They won't be committed to git
2. **They're SQLite files** - Single-file databases, easy to delete/recreate
3. **PostgreSQL is your main database** - These are just local files
4. **Tests use `test.db`** - It's automatically managed by pytest

## 🔄 Switching Between Databases

### Use PostgreSQL (Current Setup)
```env
# .env file
DATABASE_URL=postgresql://postgres:password@host:5432/postgres
```

### Use SQLite (Local Development)
```env
# .env file - comment out or remove DATABASE_URL
# DATABASE_URL=...
# App will automatically use sales.db
```

## 💡 Best Practice

Since you're using PostgreSQL:
1. ✅ Keep `DATABASE_URL` in `.env` pointing to PostgreSQL
2. ✅ You can delete `sales.db` (not needed)
3. ✅ Let `test.db` be managed by pytest (auto-created/deleted)
4. ✅ Both are already in `.gitignore` (won't be committed)

