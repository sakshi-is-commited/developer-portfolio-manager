# Sprint 03 — PostgreSQL Migration

**Sprint Goal:**
Replace the JSON-based storage system with a PostgreSQL database while maintaining the existing application architecture. This sprint focuses on introducing a production-ready database layer, implementing the Repository Pattern, and preparing the project for future backend technologies like FastAPI.

---

## Day 01 — PostgreSQL Setup & Database Foundation

### 📅 Date
21 July 2026

### 🎯 Goal

Set up PostgreSQL as the application's new storage system by creating the database, designing the project table, configuring the database connection, and preparing the repository layer for future CRUD operations.

---

### 👤 User Story

**As a developer,**

I want to replace the JSON storage system with PostgreSQL,

so that my application stores project data in a professional relational database that is scalable, maintainable, and ready for future API integration.

---

### ✅ Tasks Completed

- Installed and verified PostgreSQL.
- Installed the `psycopg2-binary` PostgreSQL driver.
- Created the `developer_portfolio` database.
- Designed and created the `projects` table.
- Added the `database/` package to the project structure.
- Created the `project_repository.py` file.
- Established and tested the PostgreSQL database connection.
- Executed SQL queries successfully to verify connectivity.
- Prepared the project architecture for migrating CRUD operations from JSON to PostgreSQL.

---

### 🏗️ Project Architecture Update

**Previous Architecture**

```
CLI
 │
 ▼
Service
 │
 ▼
JSON Storage
```

**Updated Architecture**

```
CLI
 │
 ▼
Service
 │
 ▼
Repository
 │
 ▼
PostgreSQL
```

---

### 📂 New Files Added

```
src/
└── database/
    ├── __init__.py
    ├── db.py
    ├── schema.sql
    └── project_repository.py
```

---

### 💡 Key Learnings

- Learned how PostgreSQL databases are created and managed.
- Understood how Python applications communicate with PostgreSQL using `psycopg2`.
- Learned the importance of separating database operations into a dedicated repository layer.
- Gained practical experience writing SQL table creation scripts.
- Understood why database credentials should never be hardcoded and should instead be managed using environment variables.

---

### ✔ Definition of Done

- PostgreSQL installed and running.
- Database connection established successfully.
- Database schema created.
- Repository layer added.
- SQL queries executed successfully.
- Project structure updated for database integration.

---

### 🚀 Status

**Completed ✅**

---

### 🔜 Next Step

Migrate the **Add Project** functionality from JSON storage to PostgreSQL while preserving the existing service layer.

---

# Day 02 — Add Project Migration

## 📅 Date

23 July 2026

---

## 🎯 Goal

Migrate the **Add Project** functionality from JSON storage to PostgreSQL without changing the CLI experience.

---

## 👤 User Story

**As a developer,**

I want the application to store newly created projects in PostgreSQL,

so that project data is stored securely in a relational database and the application becomes scalable and production-ready.

---

## ✅ Tasks Completed

- Implemented the `add_project()` method inside `project_repository.py`.
- Executed parameterized SQL INSERT queries.
- Added transaction commit after successful insertion.
- Implemented exception handling with rollback support.
- Ensured database connections and cursors are closed properly.
- Updated the Service Layer to use the Repository instead of JSON storage.
- Preserved the existing CLI interface without modifying the user experience.
- Successfully inserted projects into the PostgreSQL `projects` table.
- Verified inserted records using SQL queries.

---

## 🏗️ Architecture Evolution

### Previous

CLI

↓

Service

↓

JSON Storage

---

### Current

CLI

↓

Service

↓

Project Repository

↓

PostgreSQL Database

---

## 📂 Files Modified

src/

database/

- project_repository.py

services/

- project_service.py

---

## 💡 Key Learnings

- Learned how to execute parameterized SQL queries using `psycopg2`.
- Understood how the Repository Pattern isolates database operations from business logic.
- Learned how SQL transactions work using `commit()` and `rollback()`.
- Gained practical experience handling PostgreSQL exceptions.
- Reinforced the importance of keeping the CLI independent from the storage layer.

---

## 🐞 Challenges Faced

### Issue 1

```
ModuleNotFoundError: No module named 'src'
```

**Cause**

The repository file was executed directly instead of as a Python module.

**Solution**

Executed the module using:

```bash
python3 -m src.database.project_repository
```

---

### Issue 2

```
Database Error:
not all arguments converted during string formatting
```

**Cause**

Incorrect formatting while passing SQL query parameters.

**Solution**

Corrected the parameterized query structure and verified successful insertion into PostgreSQL.

---

## ✔ Definition of Done

- Repository implemented.
- Service layer updated.
- PostgreSQL insertion successful.
- SQL query verified.
- Application stores projects in PostgreSQL.
- Existing CLI functionality preserved.

---

## 🚀 Status

**Completed ✅**

---

## 🔜 Next Goal

Migrate the **View Projects** functionality from JSON storage to PostgreSQL.