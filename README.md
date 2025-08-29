# 💰 Simple Expense Tracker API (Django + PostgreSQL)

A **secure expense tracker API** built with **Django REST Framework** that allows authenticated users to manage their daily expenses with filters, summaries, and JWT authentication.

This project is based on the task **“Building a Multi-User Expense Tracker”** and demonstrates user authentication, secure expense management, and reporting with PostgreSQL as the backend.

---

## 🚀 Features
- **User Management**
  - User registration with email, password, and name.
  - JWT-based authentication (access + refresh tokens).
  - Passwords securely hashed before storage.

- **Expense Management**
  - Add, update, and delete expenses.
  - List user-specific expenses with filters (date range, category, amount range).
  - Pagination & sorting support.

- **Expense Summary**
  - Monthly expense summary grouped by category.

- **Security Measures**
  - Users can only access their own expenses (custom permission).
  - JWT authentication ensures secure access.
  - Input validation for all fields.

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/DILIP3524/expense-tracker-api.git
cd expense-tracker-api
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Activate
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL
Update `settings.py` with your PostgreSQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'expense_db',
        'USER': 'expense_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Start Development Server
```bash
python manage.py runserver
```

Visit 👉 http://127.0.0.1:8000/

---
### 8. Start Test
```bash
python manage.py test
```
Test will Start

---

## 📌 API Endpoints

### Authentication
- `POST /register/` → Register new user
- `POST /login/` → Obtain JWT token pair (access + refresh)
- `POST /login/token/refresh/` → Refresh access token

### Expenses
- `POST /expenses/` → Create expense
- `GET /expenses/` → List expenses (with filters, pagination, sorting)
- `PUT /expenses/{id}/` → Update expense
- `DELETE /expenses/{id}/` → Delete expense

### Summary
- `GET /summary/monthly/` → Get monthly summary grouped by category

---

## 🛠️ Tech Stack
- **Backend**: Django 5, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (SimpleJWT)
- **Version Control**: Git  

---

## 📂 Project Structure

```
expensetracker/
│
├── expenseapi/            # Main app (users, expenses, filters, permissions)
│   ├── models.py          # User & Expense models
│   ├── views.py           # API views
│   ├── urls.py            # API urls
│   ├── serializers.py     # DRF serializers
│   ├── permissions.py     # Custom permission: IsOwner
│   ├── filtters.py        # Expense filters
│   ├── paginations.py     # Custom pagination
│   └── tests.py           # Unit tests
│
├── expensetracker/        # Django project settings
│
├── requirements.txt       # Dependencies
├── manage.py              # Django CLI
└── README.md              # Documentation
```

---

## 👤 Author
**Dilip Kumar**  
📧 Email: dilipdev3524@gmail.com  
🐱 GitHub: [@DILIP3524](https://github.com/DILIP3524)
