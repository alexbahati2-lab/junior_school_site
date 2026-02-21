🏫 Heroes Academy Website

A modern and dynamic school website built with Django and HTML/CSS, designed for Heroes Academy — where every child is a hero in the making.

This site allows visitors to learn about the school, view galleries and upcoming events, and gives the Director a hidden admin portal to manage content directly from the site.

🚀 Features
🧩 Public Pages

Home Page — Displays the school’s mission, background slideshow of gallery photos, and highlights upcoming events.

About Page — Showcases the teachers and general school background.

Gallery Page — Displays school photos dynamically uploaded by the director.

Contact Page — Contains basic school contact information.

Events Page — Lists upcoming school events with descriptions, dates, and optional images.

🔐 Director Portal

A hidden admin area (accessible via keyboard shortcut Ctrl + Shift + D or by clicking a secret footer link).
From here, the Director can:

🏠 Edit the Home page content

🏫 Update the About page

🖼 Manage Gallery photos

📅 Add or update Events

All without needing to log into Django’s backend panel.

🧱 Tech Stack
Layer	Technology
Frontend	HTML5, CSS3, Bootstrap, JavaScript
Backend	Django 5+
Database	PostgreSQL (production) / SQLite (development)
Environment	Python 3.13 with Virtual Environment (venv)
Media Handling	Pillow (for image uploads)
Deployment	Render (automatic from GitHub)
Server	Gunicorn + WhiteNoise
⚙️ Setup Instructions
1️⃣ Clone or copy the project
git clone https://github.com/yourusername/heroes_academy_site.git
cd heroes_academy_site

2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

3️⃣ Install dependencies
pip install django pillow

4️⃣ Run database migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser (optional)
python manage.py createsuperuser

6️⃣ Start the development server
python manage.py runserver


Then open your browser and visit 👉 http://127.0.0.1:8000/

🌐 Deployment to Render

### Quick Deploy (5 minutes)
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create Web Service + PostgreSQL database
4. Set environment variables
5. Deploy! 🚀

See [QUICK_START.md](QUICK_START.md) for step-by-step instructions.

**Status**: ✅ Production-ready with PostgreSQL support

🎨 Design Notes

The homepage background automatically plays a slideshow of uploaded gallery images.

The footer link (© Heroes Academy) doubles as a hidden admin shortcut.

The Director’s portal is designed to be simple, secure, and visually integrated into the public site.

🧑‍💼 Future Enhancements

✅ Event calendar view with upcoming and past events separation

✅ Inline gallery editing and deletion

🔒 Two-factor authentication for the Director portal

🌐 Multilingual support for different regions

🧾 Printable reports for events and activities

📁 Project Structure
junior_school_site/
│
├── junior_school_site/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── main/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       ├── contact.html
│       ├── events.html
│       └── director/
│           ├── dashboard.html
│           ├── manage_gallery.html
│           ├── manage_events.html
│           └── edit_home.html
│
├── media/
│   ├── gallery/
│   └── events/
│
├── db.sqlite3
├── manage.py
└── README.md

👨‍💻 Contributors

Alex Bahati Makokha
📧 alexbahati2@gmail.com

📞 +254 726 224 423