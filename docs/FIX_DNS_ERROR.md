# Fix: "could not translate host name" Error

## 🚨 The Problem

Your computer cannot resolve the hostname `db.ecjeedhrhotncfvimjxe.supabase.co` to an IP address.

---

## ✅ Most Likely Solutions (Try in Order)

### Solution 1: Verify Hostname in Supabase Dashboard ⭐ **MOST IMPORTANT**

The hostname might be incorrect. Follow these steps:

1. **Go to Supabase Dashboard**
   - Visit: https://app.supabase.com
   - Login to your account
   - Select your project

2. **Get the Correct Connection String**
   - Click **Settings** (gear icon) in the left sidebar
   - Click **Database**
   - Scroll to **Connection string** section
   - Click on **URI** tab
   - **Copy the entire connection string**

3. **Verify the Hostname**
   - The hostname should look like: `db.xxxxxxxxxxxxx.supabase.co`
   - Make sure it matches exactly what's in your `.env` file
   - **Even one character difference will cause this error!**

4. **Update Your `.env` File**
   - Replace the entire `DATABASE_URL` with what you copied from Supabase
   - Make sure to replace `[YOUR-PASSWORD]` with your actual password

---

### Solution 2: Check if Supabase Project is Active

Supabase free tier projects **pause automatically** after 7 days of inactivity.

1. Go to https://app.supabase.com
2. Check if your project shows as **"Paused"**
3. If paused, click **"Restore"** or **"Resume"**
4. Wait a few minutes for the database to come back online
5. Try connecting again

---

### Solution 3: Use Connection Pooler URL

Supabase provides a pooler URL that might work better:

1. In Supabase Dashboard → Settings → Database
2. Look for **Connection Pooling** section
3. Copy the **Session mode** or **Transaction mode** connection string
4. It will look like:
   ```
   postgresql://postgres.xxxxx:password@aws-0-us-east-1.pooler.supabase.com:6543/postgres
   ```
5. Update your `.env` file with this URL
6. **Note:** Port is usually `6543` for pooler, not `5432`

---

### Solution 4: Check Your Internet Connection

1. **Test basic connectivity:**
   ```powershell
   ping google.com
   ```

2. **If ping fails, you have a network issue**
   - Check your internet connection
   - Try a different network (mobile hotspot)
   - Restart your router

---

### Solution 5: Try Different DNS Server

Sometimes your DNS server can't resolve the hostname. Try using Google's DNS:

1. **Change DNS settings:**
   - Open **Network Settings**
   - Change DNS to `8.8.8.8` and `8.8.4.4`
   - Or use Cloudflare DNS: `1.1.1.1` and `1.0.0.1`

2. **Flush DNS cache:**
   ```powershell
   ipconfig /flushdns
   ```

3. **Test again:**
   ```powershell
   nslookup db.ecjeedhrhotncfvimjxe.supabase.co
   ```

---

### Solution 6: Verify Project Exists

1. **Double-check the project reference ID**
   - Your hostname contains: `ecjeedhrhotncfvimjxe`
   - This should match your project's reference ID in Supabase
   - Go to project settings and verify

2. **Check if you're using the right Supabase account**
   - Make sure you're logged into the correct account
   - The project might be in a different organization

---

### Solution 7: Test with Direct Connection String from Supabase

Supabase provides connection strings in different formats. Try this:

1. In Supabase Dashboard → Settings → Database
2. Find **Connection string** → **URI**
3. Copy it exactly as shown
4. It should include `?sslmode=require` at the end
5. Replace `[YOUR-PASSWORD]` with your actual password
6. Update `.env` file

**Example format:**
```
postgresql://postgres:[YOUR-PASSWORD]@db.xxxxx.supabase.co:5432/postgres?sslmode=require
```

---

## 🔍 Diagnostic Steps

Run these commands to gather information:

```powershell
# 1. Check if .env is loaded
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('DATABASE_URL:', os.getenv('DATABASE_URL', 'NOT SET')[:100])"

# 2. Test DNS resolution
nslookup db.ecjeedhrhotncfvimjxe.supabase.co

# 3. Test network connectivity
Test-NetConnection -ComputerName db.ecjeedhrhotncfvimjxe.supabase.co -Port 5432

# 4. Run connection test
python test_db_connection.py
```

---

## ✅ Quick Checklist

Before trying anything else, verify:

- [ ] You're logged into the correct Supabase account
- [ ] The project exists and is selected
- [ ] Project is **active** (not paused)
- [ ] You copied the connection string directly from Supabase dashboard
- [ ] Hostname matches exactly (character by character)
- [ ] Password is correct (no typos, no extra spaces)
- [ ] `.env` file is in the project root directory
- [ ] `.env` file has `DATABASE_URL=` (not `DATABASE_URL =`)

---

## 🆘 Still Not Working?

### Option A: Contact Supabase Support
- Visit: https://supabase.com/support
- Check status: https://status.supabase.com

### Option B: Use SQLite for Now
If you need to test the application immediately:

1. **Comment out DATABASE_URL in `.env`:**
   ```env
   # DATABASE_URL=postgresql://...
   ```

2. **The app will use SQLite automatically**
   - Database file: `sales.db`
   - All features work the same
   - You can switch to PostgreSQL later

3. **To switch back:**
   - Uncomment the `DATABASE_URL` line
   - Fix the connection issue
   - Restart the server

---

## 📝 Correct .env Format

Your `.env` file should look exactly like this:

```env
# Database Configuration
DATABASE_URL=postgresql://postgres:your_password_here@db.ecjeedhrhotncfvimjxe.supabase.co:5432/postgres?sslmode=require
```

**Important:**
- No spaces around `=`
- Password should be URL-encoded if it has special characters
- `?sslmode=require` is required for Supabase
- Hostname must match exactly from Supabase dashboard

---

## 🎯 Most Common Fix

**90% of the time, the issue is:**
1. Hostname doesn't match Supabase dashboard exactly
2. Project is paused (needs to be resumed)
3. Connection string copied incorrectly

**Fix:** Go to Supabase Dashboard → Settings → Database → Copy the URI connection string exactly and update your `.env` file.

