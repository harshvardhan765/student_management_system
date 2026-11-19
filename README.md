# 🎓 Student Management System (SMS)

A complete, modern Web Application and RESTful API platform designed for educational institutions to manage students, teachers, courses, and attendance records with an interactive analytics dashboard.

---

## ⚡ Quick Start: How to Create Virtual Environment & Run the Code

### 🟢 Method 1: The Quick 1-Click Way (Windows)
Simply **double-click** the file:
`run_server.bat` (located in the project folder)

> It automatically detects or creates the virtual environment, installs packages, and launches the server at `http://127.0.0.1:8000/`.

---

### 💻 Method 2: Step-by-Step Manual Commands (PowerShell / Command Prompt)

Follow these exact steps from scratch:

#### Step 1: Open PowerShell / Terminal in the Project Folder
Open your terminal in:
```powershell
cd "c:\collage projrcts\student_management"
```

#### Step 2: Create the Virtual Environment
Create an isolated Python virtual environment named `venv`:
```powershell
python -m venv venv
```
*(If you have multiple Python versions installed, use: `py -3.13 -m venv venv`)*

#### Step 3: Activate the Virtual Environment
* On **Windows (PowerShell)**:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(If you see an execution policy prompt in PowerShell, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*
* On **Windows (Command Prompt / CMD)**:
  ```cmd
  venv\Scripts\activate.bat
  ```
* On **macOS / Linux**:
  ```bash
  source venv/bin/activate
  ```

#### Step 4: Install Required Packages
Install all required libraries using the provided `requirements.txt`:
```powershell
pip install -r requirements.txt
```

#### Step 5: Navigate to Inner Project & Run Migrations (Optional)
```powershell
cd student_management
python manage.py migrate
```

#### Step 6: (Optional) Run Automated Tests to Verify
```powershell
python manage.py test
```
*(You will see `Ran 4 tests ... OK`)*

#### Step 7: Run the Development Server
```powershell
python manage.py runserver 127.0.0.1:8000
```

#### Step 8: Open in Your Browser
| Page | URL |
|---|---|
| **Home Page** | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) |
| **Executive Dashboard** | [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/) |
| **Interactive API Docs (Swagger)** | [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs) |
| **Django Admin Panel** | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) |

---

## 📌 Table of Contents
1. [Project Overview](#-project-overview)
2. [Languages & Technologies Used](#-languages--technologies-used-in-depth)
3. [Key Features](#-main-features-of-the-project)
4. [Project Advantages & Benefits](#-advantages--benefits-for-easy-explanation)
5. [Code & Directory Structure](#-code--directory-structure)
6. [API Endpoints Reference](#-api-endpoints-reference)
7. [Default Login Credentials](#-default-login-credentials)

---

## 🌟 Project Overview
The **Student Management System** is a full-stack academic administration software. It unifies institutional operations by managing:
1. **Students**: Registration, personal records, roll numbers, and enrollment.
2. **Teachers**: Faculty profiles, subject specializations, qualifications, and experience.
3. **Courses**: Course catalog, course codes, credit allocations, and faculty assignments.
4. **Attendance**: Daily attendance tracking with status types (`Present`, `Absent`, `Late`, `Leave`).
5. **Dashboard**: Live visual charts summarizing data at a glance.
6. **REST API**: Fast, type-safe API endpoints with interactive Swagger documentation.

---

## 💻 Languages & Technologies Used (In-Depth)

| Layer | Language / Technology | Why & How It Is Used |
|---|---|---|
| **Core Language** | **Python 3.x** | The primary programming language used for all backend business logic, database queries, and server management. Python was chosen for its clean syntax, maintainability, and rich ecosystem. |
| **Web Framework** | **Django 5/6** | Implements the **Model-View-Template (MVT)** architecture. Django provides out-of-the-box authentication, secure session handling, Object-Relational Mapping (ORM), forms validation, and CSRF protection. |
| **API Framework** | **Django Ninja** | A modern, high-speed REST framework built on Python type annotations. It automatically generates interactive OpenAPI/Swagger documentation and performs request/response parsing up to **2x faster** than Django REST Framework (DRF). |
| **Validation Engine** | **Pydantic** | Used by Django Ninja to enforce strict data schemas. Any incoming payload with missing or invalid fields (e.g. wrong email format or invalid dates) is immediately caught and returned with clean validation messages. |
| **Database** | **SQLite3** | Relational database engine supporting ACID transactions and relational foreign keys between users, students, teachers, courses, and attendance records. |
| **Frontend Markup** | **HTML5** | Semantic HTML structure providing accessible templates across all views. |
| **Frontend Styling** | **CSS3 & Bootstrap 5** | Provides a responsive mobile-friendly grid system, cards, tables, badges, modals, and custom dashboard styles ([dashboard.css](file:///c:/collage%20projrcts/student_management/student_management/static/css/dashboard.css)). |
| **Icons** | **Bootstrap Icons** | Visual iconography used across the sidebar, action buttons, and navigation bar. |
| **Client Scripting** | **JavaScript (ES6+)** | Manages dynamic client behaviors, DOM manipulation, and chart initialization. |
| **Data Visualization** | **Chart.js** | Renders dynamic bar charts on the dashboard illustrating the number of students enrolled per course in real-time. |

---

## 🚀 Main Features of the Project

### 1. **Interactive Analytics Dashboard**
* **Instant KPI Cards**: Shows real-time counters for Total Students, Teachers, Courses, and Attendance records.
* **Enrollment Chart**: A dynamic Chart.js bar chart that graphs student enrollments per course.
* **Quick Action Shortcuts**: 1-click buttons to quickly add students, teachers, courses, or mark attendance.

### 2. **Student Management**
* **Full CRUD**: Create student profiles, view lists, edit info, and delete records.
* **Live Search**: Multi-field search filtering by name, email, roll number, or course name.
* **Pagination**: Organizes large student lists into clean pages of 10 records per page.
* **Account Sync**: Automatically creates and syncs a linked user login account.

### 3. **Teacher Management**
* Captures employee IDs, contact phone, subject specialization, qualifications, and years of experience.
* Supports assigned courses per teacher.

### 4. **Course Management**
* Manage course codes (e.g., `CS101`, `MATH201`), course titles, descriptions, and credit ratings.
* Link each course to an instructor.

### 5. **Attendance System**
* Track daily attendance per student and course.
* Status flags: `Present`, `Absent`, `Late`, `Leave`.
* **Database Unique Constraint**: Automatically prevents duplicate attendance entries for the same student, course, and date combination.

### 6. **Complete RESTful API with Swagger UI**
* Every entity (Students, Teachers, Courses, Attendance) has full REST API endpoints.
* Interactive Swagger UI at `/api/docs` allows real-time API execution directly from the browser.

---

## 💡 Advantages & Benefits (For Easy Explanation)

When explaining this project in a **viva, presentation, or interview**, here are the key talking points:

1. **Dual Interface Advantage (GUI + API)**:
   * The project isn't just a traditional website; it includes a full REST API subsystem. Web users interact via the browser, while mobile apps or third-party services can consume the same data via JSON REST endpoints.
2. **High Performance & Modern API Architecture**:
   * By using **Django Ninja** instead of traditional DRF, the API utilizes Python 3 type hinting and Pydantic, executing up to **2x faster** with zero manual serialization boilerplate.
3. **Data Consistency & Atomic Transactions**:
   * Uses `with transaction.atomic():` during student and teacher creation. If any database operation fails, all previous steps are rolled back automatically, preventing orphaned or broken user accounts.
4. **Role-Based Security**:
   * The system features an extended `User` model with built-in role differentiation (`admin`, `teacher`, `student`).
5. **Clean & Modular Code**:
   * Each major functionality is isolated in its own Django app (`accounts`, `students`, `teachers`, `courses`, `attendance`, `api`). This follows the **Separation of Concerns** principle and makes scaling effortless.

---

## 📂 Code & Directory Structure

```text
student_management/
│
├── run_server.bat              # 1-Click batch file to setup venv and launch server
├── requirements.txt            # Package dependencies (Django, django-ninja, pydantic, pillow)
├── README.md                   # Complete documentation and setup guide
│
├── venv/                       # Root Python Virtual Environment
│
└── student_management/         # Main Project Source Directory
    ├── manage.py               # Django CLI management utility
    ├── db.sqlite3              # SQLite database
    │
    ├── config/                 # Project Settings & Root URL Routing
    │   ├── settings.py         # Installed apps, middleware, database config, static paths
    │   ├── urls.py             # Global URL patterns (links apps and API routers)
    │   ├── wsgi.py             # WSGI deployment gateway
    │   └── asgi.py             # ASGI deployment gateway
    │
    ├── accounts/               # Authentication App
    │   ├── models.py           # Custom User model with roles (admin, teacher, student)
    │   ├── views.py            # Login and Logout handlers
    │   └── urls.py             # Authentication URL patterns
    │
    ├── students/               # Students App
    │   ├── models.py           # Student model (roll_number, DOB, course foreign key)
    │   ├── views.py            # Dashboard view, student search, CRUD views
    │   ├── forms.py            # Student validation forms
    │   └── urls.py             # Student URL routes
    │
    ├── teachers/               # Teachers App
    │   ├── models.py           # Teacher model (employee_id, subject, experience)
    │   ├── views.py            # Teacher CRUD views
    │   └── forms.py            # Teacher validation forms
    │
    ├── courses/                # Courses App
    │   ├── models.py           # Course model (course_code, credits, teacher foreign key)
    │   ├── views.py            # Course CRUD views
    │   └── forms.py            # Course validation forms
    │
    ├── attendance/             # Attendance App
    │   ├── models.py           # Attendance record model with unique constraints
    │   ├── views.py            # Attendance logging and history views
    │   └── forms.py            # Attendance forms
    │
    ├── api/                    # REST API App (Django Ninja)
    │   ├── api.py              # NinjaAPI root router configuration & docs setup
    │   ├── schemas.py          # Pydantic request and response schemas
    │   ├── student_api.py      # Endpoints: GET, POST, PUT, DELETE for Students
    │   ├── course_api.py       # Endpoints: GET, POST, PUT, DELETE for Courses
    │   ├── teacher_api.py      # Endpoints: GET, POST, PUT, DELETE for Teachers
    │   ├── attendance_api.py   # Endpoints: GET, POST, DELETE for Attendance
    │   └── tests.py            # Automated test suite (all tests passing)
    │
    ├── templates/              # HTML Templates
    │   ├── base.html           # Master navigation bar and layout
    │   ├── home.html           # Landing page with quick-navigation cards
    │   ├── dashboard.html      # Analytics dashboard with Chart.js
    │   ├── dashboard/layout.html # Sidebar layout with navigation links
    │   ├── accounts/           # Login templates
    │   ├── students/           # Student list, add, delete templates
    │   ├── teachers/           # Teacher list, add, delete templates
    │   ├── courses/            # Course list, add, delete templates
    │   └── attendance/         # Attendance list, add, delete templates
    │
    └── static/                 # Static Assets
        ├── css/dashboard.css   # Custom styling for dashboard, cards, sidebar
        └── js/dashboard.js     # Custom client JavaScript
```

---

## 📡 API Endpoints Reference

All endpoints return standardized JSON structures:

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
| **Home** | `GET` | `/api/` | Root API directory with links |
| **Students** | `GET` | `/api/students/` | Get all students list |
| | `GET` | `/api/students/{id}` | Get single student details |
| | `POST` | `/api/students/` | Create student and linked user |
| | `PUT` | `/api/students/{id}` | Update student details (full or partial) |
| | `DELETE`| `/api/students/{id}` | Delete student record and linked user |
| **Courses** | `GET` | `/api/courses/` | Get all courses |
| | `GET` | `/api/courses/{id}` | Get course by ID |
| | `POST` | `/api/courses/` | Create new course |
| | `PUT` | `/api/courses/{id}` | Update course |
| | `DELETE`| `/api/courses/{id}` | Delete course |
| **Teachers** | `GET` | `/api/teachers/` | Get all teachers |
| | `GET` | `/api/teachers/{id}` | Get teacher by ID |
| | `POST` | `/api/teachers/` | Create new teacher |
| | `PUT` | `/api/teachers/{id}` | Update teacher details |
| | `DELETE`| `/api/teachers/{id}` | Delete teacher |
| **Attendance** | `GET`| `/api/attendance/` | Get all attendance logs |
| | `GET` | `/api/attendance/{id}`| Get attendance record by ID |
| | `POST` | `/api/attendance/` | Mark daily attendance |
| | `DELETE`| `/api/attendance/{id}`| Remove attendance log |

---

## 🔑 Default Login Credentials

* **Role**: Administrator
* **Username**: `admin`
* *(You can also create a new admin at any time by running `python manage.py createsuperuser`)*
