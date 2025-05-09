
## Student Admission Portal (Flask)

This is a web-based student admission system built using **Python**, **Flask**, and **SQLAlchemy**. It allows students to apply for admission by submitting personal and academic details, and enables admins to review, approve, and generate PDF admission letters.

---

## Features

- Student application form with file uploads (degree certificate, ID proof)
- Admin review interface to approve/reject applications
- Auto-generation of admission letter as downloadable PDF upon approval
- Form validation and document handling
- SQLite support by default, with optional MySQL integration
- Test-Driven Development (TDD) setup
- Follows clean project structure and development practices

---

## 📂 Project Structure

```

student\_admission\_app/
├── app/
│   ├── static/                   # Static files (CSS, PDFs)
│   ├── templates/                # HTML templates
│   ├── **init**.py               # App factory
│   ├── models.py                 # SQLAlchemy models
│   ├── routes.py                 # Flask routes
│   ├── forms.py                  # WTForms or basic validators
│   ├── pdf\_generator.py          # PDF generation logic
├── migrations/                   # Database migration files
├── tests/                        # Unit tests
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables
├── run.py                        # Entry point
├── README.md                     # This file

````

---

## 🛠️ How to Run

### 1. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate  # On macOS/Linux
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Run the Flask app

```bash
flask run
```

Visit:

* Student Form: [http://127.0.0.1:5000/student/apply](http://127.0.0.1:5000/student/apply)
* Admin UI: [http://127.0.0.1:5000/admin/review](http://127.0.0.1:5000/admin/review)

---

## Switching to MySQL

To use MySQL instead of SQLite:

1. Update the `.env` file:

```
DATABASE_URL = mysql://username:password@localhost/db_name
```

2. Run migrations again:

```bash
flask db migrate -m "Switch to MySQL"
flask db upgrade
```

---

## 🧪 Testing

```bash
pytest
```

All unit tests are inside the `tests/` directory.

---

## 📄 Functional Requirement Document (FRD)

See `docs/Functional_Requirement_Document.md` for detailed functionality, assumptions, and user workflows.

---

## 🧪 Test-Driven Development (TDD)

All core features are written and tested using TDD practices. New features should be covered by test cases.

---

## 📦 Technology Stack

* **Backend**: Python, Flask
* **Database**: SQLite (default), MySQL (optional)
* **ORM**: SQLAlchemy
* **Migrations**: Flask-Migrate (Alembic)
* **PDF Generation**: ReportLab
* **Templating**: Jinja2
* **Testing**: PyTest

---


