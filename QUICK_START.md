# Quick Start Guide: PostgreSQL & Render Deployment

## 🎯 What's Changed?
Your project is now configured for professional deployment with:
- ✅ PostgreSQL database support
- ✅ Production-ready security settings
- ✅ Automatic deployment configuration
- ✅ Environment variable management

## 🚀 Deploy to Render in 5 Minutes

### 1. Set Up GitHub (if not already done)
```bash
git init
git add .
git commit -m "Configure PostgreSQL and production settings for Render"
git remote add origin https://github.com/yourusername/junior_school_site.git
git push -u origin main
```

### 2. Go to Render.com
- Sign up or log in to [render.com](https://render.com)
- Connect your GitHub account

### 3. Create Web Service
1. Click "New +" → "Web Service"
2. Select your repository
3. Fill in:
   - **Name**: `junior-school-site`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn junior_school_site.wsgi:application`
4. Click "Create Web Service"

### 4. Create PostgreSQL Database
1. During/after web service creation, click "New +" → "PostgreSQL"
2. Fill in name: `junior-school-db`
3. Click "Create Database"
4. Copy the connection string

### 5. Add Environment Variables
In your web service, go to "Environment" and add:
```
SECRET_KEY=use-a-secure-key-generator
DEBUG=False
ALLOWED_HOSTS=yourdomain.onrender.com
DATABASE_URL=(paste from PostgreSQL)
CSRF_TRUSTED_ORIGINS=https://yourdomain.onrender.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### 6. Deploy!
Push to GitHub and Render will automatically deploy:
```bash
git push origin main
```
Done! Your site is live! 🎉

## 💻 Local Development

### First Time Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Edit .env and set DEBUG=True

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

### Regular Development
```bash
# Just run the server
python manage.py runserver

# Visit http://localhost:8000
```

## 📱 Access Director Portal
- Production: `https://yourdomain.onrender.com/director/login/`
- Local: `http://localhost:8000/director/login/`

## 🔐 Generate Secure SECRET_KEY
Use this Python code:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use online tools like: https://djecrety.ir/

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named..."
```bash
pip install -r requirements.txt
```

### Static files not showing
```bash
python manage.py collectstatic --noinput
```

### Database connection error
- Check `DATABASE_URL` is set correctly
- Verify PostgreSQL database is running (on Render)

### Render deployment fails
- Check build logs in Render dashboard
- Ensure all files are committed to Git
- Run `python manage.py check` locally first

## 📚 Full Documentation
See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions.

## ✨ That's It!
Your site is now production-ready! 🚀
