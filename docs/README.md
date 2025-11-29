# Documentation Index

This directory contains all documentation for the Sales Insights Backend project.

## 📚 Available Documentation

### Getting Started
- **[Quick Start Guide](QUICK_START.md)** - Get up and running in 5 minutes
- **[Setup Guide](SETUP_GUIDE.md)** - Comprehensive setup instructions with detailed steps

### Troubleshooting
- **[Database Troubleshooting](TROUBLESHOOTING_DB.md)** - General database connection issues
- **[Fix DNS Error](FIX_DNS_ERROR.md)** - Resolve "could not translate host name" errors
- **[Use Pooler Connection](USE_POOLER_CONNECTION.md)** - Use Supabase connection pooler

## 🎯 Which Guide Should I Read?

- **First time setting up?** → Start with [Quick Start Guide](QUICK_START.md)
- **Need detailed instructions?** → Read [Setup Guide](SETUP_GUIDE.md)
- **Having database connection issues?** → Check [Database Troubleshooting](TROUBLESHOOTING_DB.md)
- **Getting DNS errors?** → See [Fix DNS Error](FIX_DNS_ERROR.md)
- **Using Supabase?** → Try [Use Pooler Connection](USE_POOLER_CONNECTION.md)

## 📖 Quick Reference

### Common Commands
```bash
# Start server
uvicorn app.main:app --reload

# Test database connection
python scripts/test_db_connection.py

# Seed sample data
python scripts/seed.py

# Run tests
pytest
```

### Important Files
- `.env` - Environment variables (create from `.env.example`)
- `postman/Sales_Insights_API.postman_collection.json` - Postman API collection
- `scripts/seed.py` - Seed database with sample data

