"""
Simple script to test PostgreSQL database connection.
Run this to verify your DATABASE_URL is configured correctly.
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    from sqlalchemy import create_engine, text
    from app.database import DATABASE_URL, engine
    
    print("=" * 60)
    print("Database Connection Test")
    print("=" * 60)
    print(f"\nDatabase URL: {DATABASE_URL.split('@')[0]}@[HIDDEN]")
    print(f"Database Type: {'PostgreSQL' if 'postgresql' in DATABASE_URL else 'SQLite'}")
    
    # Test connection
    print("\nAttempting to connect...")
    with engine.connect() as conn:
        if 'postgresql' in DATABASE_URL:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"✅ Connection successful!")
            print(f"PostgreSQL Version: {version.split(',')[0]}")
            
            # Test if tables exist
            result = conn.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """))
            tables = [row[0] for row in result.fetchall()]
            
            if tables:
                print(f"\n✅ Found {len(tables)} table(s):")
                for table in tables:
                    print(f"   - {table}")
            else:
                print("\n⚠️  No tables found. Run the application to create them.")
        else:
            print("✅ SQLite connection successful!")
            print("Note: Using SQLite database (local file)")
    
    print("\n" + "=" * 60)
    print("✅ Database connection test PASSED!")
    print("=" * 60)
    
except Exception as e:
    print("\n" + "=" * 60)
    print("❌ Database connection test FAILED!")
    print("=" * 60)
    print(f"\nError: {str(e)}")
    
    # Provide specific troubleshooting based on error type
    error_str = str(e).lower()
    
    if "could not translate host name" in error_str or "name or service not known" in error_str:
        print("\n🔍 DNS Resolution Issue Detected!")
        print("\nPossible causes:")
        print("1. Hostname is incorrect - verify in Supabase dashboard")
        print("2. Network connectivity issue - check internet connection")
        print("3. DNS server issue - try different DNS (8.8.8.8)")
        print("4. Firewall blocking - check Windows Firewall")
        print("5. Supabase project might be paused - check dashboard")
        print("\nQuick fixes:")
        print("- Verify connection string in Supabase: Settings → Database")
        print("- Try using pooler URL if available")
        print("- Check if project is active (not paused)")
    elif "password authentication failed" in error_str:
        print("\n🔍 Authentication Issue!")
        print("- Verify password is correct")
        print("- Check if password needs URL encoding")
        print("- Ensure no extra spaces in password")
    elif "connection refused" in error_str or "timeout" in error_str:
        print("\n🔍 Connection Issue!")
        print("- Check if port 5432 is accessible")
        print("- Verify firewall settings")
        print("- Try using pooler connection (port 6543)")
    else:
        print("\nTroubleshooting:")
        print("1. Check your .env file exists and has DATABASE_URL")
        print("2. Verify your database password is correct")
        print("3. Ensure your Supabase database is accessible")
        print("4. Check if special characters in password need URL encoding")
        print("5. See TROUBLESHOOTING_DB.md for detailed help")
    
    print("\n💡 Tip: Run 'python -c \"from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv(\\\"DATABASE_URL\\\", \\\"NOT SET\\\"))\"' to verify .env is loaded")
    sys.exit(1)

