# STOCKS

# STOCKS

A simple Stocks Management System built using Python Django, demonstrating clean implementation of CRUD operations (Create, Read, Update, Delete) for managing stock items.

This project is ideal as a beginner-friendly Django application to practice working with models, views, templates, and forms while applying Object-Oriented Programming (OOP) principles.

🚀 Features
Add new stock items with name, category, quantity, and price.

View a list of all stocks in the system.

Edit existing stock details.

Delete stocks from the inventory.

Clean and responsive HTML templates using Django’s templating engine.

Fully written in Python with Django’s MVC (MTV) architecture.

🛠️ Tech Stack
Backend: Python 3.x, Django 4.x

Database: SQLite3 (default Django DB)

Frontend: HTML5, CSS (optional Bootstrap for styling)

📂 Project Structure
bash
Copy
Edit
stocks_management/
├── stocks/              # Django app with models, views, urls, templates
│   ├── migrations/
│   ├── templates/stocks/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── stocks_management/   # Project settings
├── db.sqlite3
└── manage.py
⚙️ Setup & Run
1️⃣ Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/stocks-management-django.git
cd stocks-management-django
2️⃣ Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run migrations and start the server:

bash
Copy
Edit
python manage.py migrate
python manage.py runserver
5️⃣ Open your browser at:
http://127.0.0.1:8000/stocks/

👨‍💻 Author
Dhejeswara V

