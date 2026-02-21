# PostgreSQL Migration & Render Deployment Guide

## Changes Made

### 1. **Database Migration to PostgreSQL**
   - Updated `requirements.txt` with PostgreSQL adapter (`psycopg2-binary`)
   - Added `dj-database-url` for environment-based configuration
   - Added `python-decouple` for secure environment variable management
   - `settings.py` now detects `DATABASE_URL` environment variable and uses PostgreSQL when available

### 2. **Production Ready Configuration**
   - Removed hardcoded `SECRET_KEY` - now uses environment variable
   - `DEBUG` mode now controlled by environment variable (defaults to `False`)
   - `ALLOWED_HOSTS` now configurable via environment variable
   - Added `whitenoise` middleware for static file serving in production
   - Added `STATIC_ROOT` configuration for collectstatic command
   - Added security settings (SSL, HSTS, CSRF cookie protection)

### 3. **Deployment Files**
   - **Procfile** - Specifies release and web process commands for Render
   - **render.yaml** - Complete Render deployment configuration
   - **.env.example** - Template for environment variables
   - **.gitignore** - Prevents committing sensitive files

### 4. **Bugs Fixed**
   - ✅ Missing `STATIC_ROOT` - added for production static file collection
   - ✅ Missing `STATICFILES_STORAGE` - added WhiteNoise compression
   - ✅ Insecure SECRET_KEY exposed in repository - moved to environment variable
   - ✅ No production logging configuration - added console logging for Render

## Local Development Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create .env file (local development)
```bash
cp .env.example .env
```

Edit `.env` and set:
```
SECRET_KEY=your-dev-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 5. Create Superuser (if needed)
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver
```

## Deployment to Render

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Configure PostgreSQL and production settings"
git push origin main
```

### Step 2: Create New Web Service on Render
1. Go to [render.com](https://render.com)
2. Create new "Web Service"
3. Connect your GitHub repository
4. Set the following:
   - **Name**: junior-school-site
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn junior_school_site.wsgi:application`

### Step 3: Create PostgreSQL Database on Render
1. Create new "PostgreSQL" database
2. Copy the connection string (DATABASE_URL)

### Step 4: Add Environment Variables
In Render dashboard, add these environment variables:
```
SECRET_KEY=<generate a new secret key>
DEBUG=False
ALLOWED_HOSTS=yourdomain.onrender.com,www.yourdomain.onrender.com
DATABASE_URL=<paste from PostgreSQL database>
CSRF_TRUSTED_ORIGINS=https://yourdomain.onrender.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
```

### Step 5: Deploy
1. Render automatically deploys when you push to GitHub
2. Watch the deployment logs in Render dashboard
3. Once deployed, visit your domain

## Switching Back to SQLite (Local Development)
If you want to use SQLite locally:
1. Simply don't set `DATABASE_URL` environment variable
2. Or set it to empty string in `.env`
3. Django will automatically use SQLite

## Important Notes
- **Never commit `.env` file** - it contains sensitive data (already in .gitignore)
- **Generate new SECRET_KEY** for production - use a secure generator
- **Media files** are stored in `/media` folder - configure Render storage if needed for persistence
- **Static files** are automatically collected and served by WhiteNoise
- **Database backups** - set up automatic backups in Render PostgreSQL settings

## Testing the Migration Locally
To test PostgreSQL locally before deploying:

1. Install PostgreSQL locally
2. Create a database: `createdb junior_school_db`
3. Set environment variable:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/junior_school_db
   ```
4. Run migrations: `python manage.py migrate`
5. Test all features before deploying to Render

## Troubleshooting

### Static files not loading
- Run `python manage.py collectstatic --noinput`
- Check `STATIC_ROOT` directory is created

### Database connection errors
- Verify `DATABASE_URL` is correctly set
- Check PostgreSQL is running (if testing locally)
- Verify credentials in connection string

### Migrations fail
- Ensure all migrations are committed to GitHub
- Check migration files in `main/migrations/` and `director/migrations/`

## Additional Security Recommendations
1. Use a secrets manager for sensitive data
2. Enable HTTPS only (SECURE_SSL_REDIRECT=True)
3. Set strong CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE
4. Regularly update Django and dependencies
5. Consider adding rate limiting for the director login
