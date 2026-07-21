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