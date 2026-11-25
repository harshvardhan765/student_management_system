# 🎓 Student Management System (SMS)

A complete, modern Web Application and RESTful API platform designed for educational institutions to manage students, teachers, courses, and attendance records with an interactive analytics dashboard.

---

## ⚠️ Python Version Requirement (Important Note)

> **Recommended Interpreter**: **Python 3.12** or **Python 3.13** (64-bit).
> 
> **Why not Python 3.14?**  
> `pydantic-core` (the Rust engine underlying Pydantic and Django Ninja) does not yet supply pre-compiled binary `.pyd` wheels for Python 3.14 on Windows. Attempting to run with Python 3.14 results in:
> `ImportError: cannot import name 'ArgsKwargs' from 'pydantic_core._pydantic_core'`
> 
> The virtual environment for this project is configured to run on **Python 3.13** using the exact compatible pinned wheels.

---

## ⚡ Quick Start: How to Run the Project

### 🟢 Method 1: The 1-Click Launch (Windows)
Simply **double-click** the file:
`run_server.bat` (located in the project root folder)

> It automatically detects the Python 3.13 virtual environment, verifies dependencies from `requirements.txt`, and launches the development server at `http://127.0.0.1:8000/`.

---

### 💻 Method 2: Step-by-Step Manual Setup (PowerShell / Command Prompt)

Follow these exact steps from scratch:

#### Step 1: Open PowerShell / Terminal in the Project Root
```powershell
cd "c:\collage projrcts\student_management"
```

#### Step 2: Create the Virtual Environment (Using Python 3.13)
```powershell
py -3.13 -m venv venv
```
*(Or `py -3.12 -m venv venv` if using Python 3.12)*

#### Step 3: Activate the Virtual Environment
* On **Windows (PowerShell)**:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(If you encounter a PowerShell script execution policy restriction, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*
* On **Windows (Command Prompt / CMD)**:
  ```cmd
  venv\Scripts\activate.bat
  ```
* On **macOS / Linux**:
  ```bash
  source venv/bin/activate
  ```

#### Step 4: Install Required Packages
Install all exact, pinned working libraries:
```powershell
pip install -r requirements.txt
```

#### Step 5: (Optional) Configure Environment Variables
Copy `.env.example` to `.env`:
```powershell
copy .env.example .env
```

#### Step 6: Apply Database Migrations
```powershell
cd student_management
python manage.py makemigrations
python manage.py migrate
```

#### Step 7: Run System Checks & Automated Tests
```powershell
python manage.py check
python manage.py test
```
*(All 4 test suites will execute and pass: `Ran 4 tests ... OK`)*

#### Step 8: Start the Development Server
```powershell
python manage.py runserver 127.0.0.1:8000
```

#### Step 9: Open in Your Browser
| Page | URL |
|---|---|
| **Home Page** | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) |
| **Executive Dashboard** | [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/) |
| **Interactive API Docs (Swagger)** | [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs) |
| **OpenAPI Schema (JSON)** | [http://127.0.0.1:8000/api/openapi.json](http://127.0.0.1:8000/api/openapi.json) |
| **Django Admin Panel** | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) |

---

## 📌 Table of Contents
1. [Languages & Technologies Used](#-languages--technologies-used)
2. [Main Features](#-main-features)
3. [Advantages & Benefits](#-advantages--benefits-for-viva--presentations)
4. [Code & Directory Structure](#-code--directory-structure)
5. [API Endpoints Reference](#-api-endpoints-reference)
6. [Default Login Credentials](#-default-login-credentials)

---

## 💻 Languages & Technologies Used

| Component | Technology | Description |
|---|---|---|
| **Programming Language** | **Python 3.13** | Core backend language powering data processing, routing, and APIs. |
| **Web Framework** | **Django 6.x** | Model-View-Template (MVT) architecture, ORM, authentication, and session handling. |
| **API Framework** | **Django Ninja (v1.8)** | High-performance FastAPI-like REST framework built on type hints and Pydantic. |
| **Validation Engine** | **Pydantic (v2.14) & pydantic-core (v2.50)** | Fast data serialization, parsing, and strict input/output validation. |
| **Database** | **SQLite3** | Relational database with foreign keys, transactional integrity, and ACID compliance. |
| **Frontend Styling** | **HTML5, CSS3, Bootstrap 5** | Fully responsive web interface with cards, modals, tables, and sidebar layout. |
| **Data Visualization** | **Chart.js** | Interactive client-side bar charts displaying course enrollment distribution. |

---

## 🚀 Main Features

1. **Executive Dashboard & Analytics**: Real-time KPI summary cards and dynamic enrollment bar charts.
2. **Student Management**: Full CRUD, live multi-field search (name, email, roll number, course), pagination, and linked user authentication.
3. **Teacher Management**: Complete teacher directory tracking employee IDs, subject specializations, qualifications, and years of experience.
4. **Course Management**: Course catalog with course codes, credit units, descriptions, and assigned faculty instructors.
5. **Attendance System**: Daily student attendance logging with status options (`Present`, `Absent`, `Late`, `Leave`) and duplicate-prevention constraints.
6. **RESTful APIs with Swagger UI**: Auto-generated interactive OpenAPI / Swagger documentation at `/api/docs` enabling live API testing without Postman.

---

## 💡 Advantages & Benefits (For Viva / Presentations)

1. **Dual Architecture (MVT GUI + REST API)**: Web users manage records via the browser, while external client apps or mobile applications can connect via JSON endpoints.
2. **Type Safety & Automatic Validation**: Pydantic validates all incoming parameters before hitting database handlers.
3. **Atomic Database Transactions**: `transaction.atomic()` prevents partial writes and database corruption.
4. **High Performance**: Django Ninja executes significantly faster than traditional Django REST Framework (DRF).
5. **Clean Modular Structure**: Separation of Concerns across individual Django apps (`accounts`, `students`, `teachers`, `courses`, `attendance`, `api`).

---

## 📂 Code & Directory Structure

```text
student_management/
│
├── run_server.bat              # 1-Click batch file to start the server
├── requirements.txt            # Exact pinned package dependencies
├── .env.example                # Example environment variables template
├── .gitignore                  # Git exclusion rules
├── README.md                   # Project documentation and setup guide
│
├── venv/                       # Python 3.13 Virtual Environment
│
└── student_management/         # Main Project Source Directory
    ├── manage.py               # Django CLI management script
    ├── db.sqlite3              # Relational SQLite database
    │
    ├── config/                 # Project Settings & Root Routing
    │   ├── settings.py         # App configuration & environment loader
    │   ├── urls.py             # Global URL patterns (connects UI & REST APIs)
    │   ├── wsgi.py             # WSGI gateway
    │   └── asgi.py             # ASGI gateway
    │
    ├── accounts/               # Authentication App
    │   ├── models.py           # Custom User model (roles: admin, teacher, student)
    │   ├── views.py            # Login & Logout handlers
    │   └── urls.py             # Auth URL routes
    │
    ├── students/               # Students App
    │   ├── models.py           # Student model (roll_number, DOB, course FK)
    │   ├── views.py            # Dashboard view, search, student CRUD
    │   ├── forms.py            # Student validation forms
    │   └── urls.py             # Student URL routes
    │
    ├── teachers/               # Teachers App
    │   ├── models.py           # Teacher model (employee_id, subject, experience)
    │   ├── views.py            # Teacher CRUD views
    │   └── forms.py            # Teacher validation forms
    │
    ├── courses/                # Courses App
    │   ├── models.py           # Course model (course_code, credits, teacher FK)
    │   ├── views.py            # Course CRUD views
    │   └── forms.py            # Course validation forms
    │
    ├── attendance/             # Attendance App
    │   ├── models.py           # Attendance record model with unique constraints
    │   ├── views.py            # Attendance logging views
    │   └── forms.py            # Attendance forms
    │
    ├── api/                    # REST API Subsystem (Django Ninja)
    │   ├── api.py              # NinjaAPI root router configuration & docs setup
    │   ├── schemas.py          # Pydantic request and response schemas
    │   ├── student_api.py      # Endpoints: GET, POST, PUT, DELETE for Students
    │   ├── course_api.py       # Endpoints: GET, POST, PUT, DELETE for Courses
    │   ├── teacher_api.py      # Endpoints: GET, POST, PUT, DELETE for Teachers
    │   ├── attendance_api.py   # Endpoints: GET, POST, DELETE for Attendance
    │   └── tests.py            # Automated test suite (all tests passing)
    │
    ├── templates/              # HTML Templates
    │   ├── base.html           # Master navigation layout
    │   ├── home.html           # Landing home page with quick links
    │   ├── dashboard.html      # Analytics dashboard with Chart.js
    │   └── dashboard/layout.html # Sidebar dashboard layout
    │
    └── static/                 # Static Assets
        ├── css/dashboard.css   # Custom dashboard styling
        └── js/dashboard.js     # Dashboard client scripts
```

---

## 📡 API Endpoints Reference

All endpoints return JSON formatted with standardized response envelopes:

```json
{
  "status": true,
  "message": "Operation successful.",
  "data": { ... }
}
```

| Domain | HTTP Method | Endpoint | Description |
|---|---|---|---|
| **Docs** | `GET` | `/api/docs` | Interactive Swagger UI Documentation |
| **Schema** | `GET` | `/api/openapi.json` | OpenAPI JSON specification |
| **Root** | `GET` | `/api/` | Root API directory with links |
| **Students** | `GET` | `/api/students/` | Get all students |
| | `GET` | `/api/students/{id}` | Get student by ID |
| | `POST` | `/api/students/` | Create student and linked user account |
| | `PUT` | `/api/students/{id}` | Update student details (full or partial) |
| | `DELETE`| `/api/students/{id}` | Delete student and linked user |
| **Courses** | `GET` | `/api/courses/` | Get all courses |
| | `GET` | `/api/courses/{id}` | Get course by ID |
| | `POST` | `/api/courses/` | Create course |
| | `PUT` | `/api/courses/{id}` | Update course |
| | `DELETE`| `/api/courses/{id}` | Delete course |
| **Teachers** | `GET` | `/api/teachers/` | Get all teachers |
| | `GET` | `/api/teachers/{id}` | Get teacher by ID |
| | `POST` | `/api/teachers/` | Create teacher |
| | `PUT` | `/api/teachers/{id}` | Update teacher details |
| | `DELETE`| `/api/teachers/{id}` | Delete teacher |
| **Attendance** | `GET`| `/api/attendance/` | Get all attendance records |
| | `GET` | `/api/attendance/{id}`| Get attendance record by ID |
| | `POST` | `/api/attendance/` | Log attendance record |
| | `DELETE`| `/api/attendance/{id}`| Delete attendance record |

---

## 🔑 Default Login Credentials

* **Role**: Administrator
* **Username**: `admin`
* *(To create another admin account at any time, run: `python manage.py createsuperuser`)*
