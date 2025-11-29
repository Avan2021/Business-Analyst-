# Database Connection Troubleshooting Guide

## Error: "could not translate host name"

This error means your computer cannot resolve the database hostname to an IP address.

---

## ✅ Solution 1: Verify Your Supabase Connection String

1. **Go to your Supabase Dashboard**
   - Visit: https://app.supabase.com
   - Select your project
   - Go to **Settings** → **Database**
   - Find the **Connection string** section

2. **Copy the correct connection string**
   - Use the **URI** format (not the other formats)
   - It should look like: `postgresql://postgres:[YOUR-PASSWORD]@db.xxxxx.supabase.co:5432/postgres`

3. **Verify the hostname matches**
   - Your hostname: `db.ecjeedhrhotncfvimjxe.supabase.co`
   - Make sure this matches exactly what's in your Supabase dashboard

---

## ✅ Solution 2: Use Explicit Driver in Connection String

Update your `.env` file to use the explicit `psycopg2` driver:

```env
DATABASE_URL=postgresql+psycopg2://postgres:ajkdfwefbdsnfbajsf@db.ecjeedhrhotncfvimjxe.supabase.co:5432/postgres?sslmode=require
```

**Note:** Changed `postgresql://` to `postgresql+psycopg2://`

---

## ✅ Solution 3: Check Network Connectivity

### Test DNS Resolution:
```powershell
nslookup db.ecjeedhrhotncfvimjxe.supabase.co
```

### Test Connectivity:
```powershell
Test-NetConnection -ComputerName db.ecjeedhrhotncfvimjxe.supabase.co -Port 5432
```

**Expected:** Should show `TcpTestSucceeded : True`

---

## ✅ Solution 4: Verify Supabase Project Status

1. **Check if project is active**
   - Go to Supabase dashboard
   - Ensure project is not paused
   - Supabase free tier projects pause after inactivity

2. **Check database status**
   - In Supabase dashboard, verify database is running
   - Look for any error messages

---

## ✅ Solution 5: Try Alternative Connection String Format

Sometimes Supabase provides connection strings in different formats. Try this format:

```env
DATABASE_URL=postgresql+psycopg2://postgres.ecjeedhrhotncfvimjxe:ajkdfwefbdsnfbajsf@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require
```

**Note:** This uses the pooler connection. Check your Supabase dashboard for the exact pooler URL.

---

## ✅ Solution 6: Check Firewall/Antivirus

1. **Windows Firewall**
   - Ensure it's not blocking outbound connections
   - Try temporarily disabling to test

2. **Antivirus Software**
   - Some antivirus software blocks database connections
   - Add exception for Python/your application

3. **Corporate Network**
   - If on corporate network, port 5432 might be blocked
   - Contact IT to whitelist the Supabase hostname

---

## ✅ Solution 7: Use Direct IP (If Available)

If Supabase provides a direct IP address in the dashboard, you can try using that instead of the hostname.

**Note:** IP addresses can change, so this is not recommended for production.

---

## ✅ Solution 8: Test with psql Command Line Tool

Install PostgreSQL client and test connection directly:

```powershell
# Install PostgreSQL client (if not installed)
# Download from: https://www.postgresql.org/download/windows/

# Test connection
psql "postgresql://postgres:ajkdfwefbdsnfbajsf@db.ecjeedhrhotncfvimjxe.supabase.co:5432/postgres?sslmode=require"
```

If this works, the issue is with the Python/SQLAlchemy setup.
If this fails, the issue is with network/credentials.

---

## ✅ Solution 9: Update Database Configuration

I've updated `app/database.py` to automatically use the `psycopg2` driver. Make sure your `.env` file has:

```env
DATABASE_URL=postgresql://postgres:ajkdfwefbdsnfbajsf@db.ecjeedhrhotncfvimjxe.supabase.co:5432/postgres?sslmode=require
```

The code will automatically convert it to use `postgresql+psycopg2://`.

---

## ✅ Solution 10: Verify Password Encoding

If your password has special characters, ensure they're properly encoded:

```powershell
# Test password encoding
python -c "from urllib.parse import quote; print(quote('ajkdfwefbdsnfbajsf'))"
```

If the password contains special characters, use the encoded version in the URL.

---

## 🔍 Diagnostic Commands

Run these to gather information:

```powershell
# 1. Test DNS
nslookup db.ecjeedhrhotncfvimjxe.supabase.co

# 2. Test port connectivity
Test-NetConnection -ComputerName db.ecjeedhrhotncfvimjxe.supabase.co -Port 5432

# 3. Test with Python
python test_db_connection.py

# 4. Check environment variable
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('DATABASE_URL', 'NOT SET'))"
```

---

## 📋 Checklist

- [ ] Verified connection string in Supabase dashboard
- [ ] Hostname matches exactly
- [ ] Password is correct (no extra spaces)
- [ ] Using `postgresql+psycopg2://` or letting code auto-convert
- [ ] `sslmode=require` is in the URL
- [ ] Network connectivity test passes
- [ ] Supabase project is active (not paused)
- [ ] Firewall/antivirus not blocking
- [ ] Tested with `psql` command line tool

---

## 🆘 Still Not Working?

1. **Double-check Supabase Dashboard**
   - Go to Settings → Database
   - Copy the connection string directly from there
   - Make sure you're using the correct project

2. **Try Connection Pooling URL**
   - Supabase provides a pooler URL
   - Usually ends with `.pooler.supabase.com`
   - Port might be 6543 instead of 5432

3. **Contact Support**
   - Supabase support: https://supabase.com/support
   - Check Supabase status page: https://status.supabase.com

---

## 💡 Quick Fix: Use SQLite for Testing

If you need to test the application immediately while fixing PostgreSQL:

1. Remove or comment out `DATABASE_URL` in `.env`
2. The app will automatically use SQLite (`sales.db`)
3. You can switch back to PostgreSQL later

```env
# DATABASE_URL=postgresql://...
```

