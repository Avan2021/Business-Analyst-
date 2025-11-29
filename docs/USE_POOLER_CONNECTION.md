# Use Supabase Connection Pooler (Recommended Fix)

## 🎯 The Solution

Your hostname resolves but your system DNS might have issues. **Supabase Connection Pooler** is more reliable and often works better.

---

## ✅ Step-by-Step Instructions

### Step 1: Get Pooler URL from Supabase

1. **Go to Supabase Dashboard**
   - Visit: https://app.supabase.com
   - Select your project
   - Go to **Settings** → **Database**

2. **Find Connection Pooling Section**
   - Scroll down to **Connection Pooling**
   - You'll see two modes:
     - **Session mode** (recommended for most cases)
     - **Transaction mode** (for serverless)

3. **Copy the Connection String**
   - Click on **Session mode** tab
   - Copy the **URI** connection string
   - It will look like:
     ```
     postgresql://postgres.ecjeedhrhotncfvimjxe:YOUR_PASSWORD@aws-0-us-east-1.pooler.supabase.com:6543/postgres
     ```
   - **Note:** Port is `6543` (not `5432`)
   - **Note:** Hostname uses `.pooler.supabase.com` (not direct connection)

---

### Step 2: Update Your .env File

Replace your current `DATABASE_URL` with the pooler connection string:

```env
# Database Configuration - Using Connection Pooler (Recommended)
DATABASE_URL=postgresql://postgres.ecjeedhrhotncfvimjxe:ajkdfwefbdsnfbajsf@aws-0-us-east-1.pooler.supabase.com:6543/postgres?sslmode=require
```

**Important:**
- Replace `ajkdfwefbdsnfbajsf` with your actual password
- The exact pooler hostname might be different (check Supabase dashboard)
- Port is `6543` for pooler
- Keep `?sslmode=require` at the end

---

### Step 3: Test the Connection

```powershell
python test_db_connection.py
```

**Expected:** ✅ Connection successful!

---

## 🔍 Why Pooler Works Better

1. **Better DNS Resolution** - Pooler URLs are more stable
2. **Connection Management** - Handles connections more efficiently
3. **IPv4 Support** - Often has better IPv4 connectivity
4. **Recommended by Supabase** - Official recommended method

---

## 📋 Alternative: Direct Connection (If Pooler Doesn't Work)

If you must use direct connection, try these fixes:

### Option A: Use IPv4 Explicitly

Update your `.env` to use the IPv4 address directly (if you can get it):

```env
# First, get the IP address
# Run: nslookup db.ecjeedhrhotncfvimjxe.supabase.co 8.8.8.8
# Then use the IPv4 address if available
DATABASE_URL=postgresql://postgres:password@[IP_ADDRESS]:5432/postgres?sslmode=require
```

**Note:** IP addresses can change, so this is not recommended for production.

### Option B: Fix DNS on Your System

1. **Change DNS to Google DNS:**
   - Open **Network Settings**
   - Change DNS to `8.8.8.8` and `8.8.4.4`
   - Flush DNS: `ipconfig /flushdns`

2. **Restart your computer**

3. **Test again:**
   ```powershell
   python test_db_connection.py
   ```

---

## ✅ Quick Test Commands

```powershell
# Test pooler hostname resolution
nslookup aws-0-us-east-1.pooler.supabase.com

# Test connection
python test_db_connection.py

# Verify .env is loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('URL:', os.getenv('DATABASE_URL', 'NOT SET')[:100])"
```

---

## 🎯 Recommended Action

**Use the Connection Pooler URL from Supabase Dashboard** - it's the most reliable solution and what Supabase recommends for production use.

