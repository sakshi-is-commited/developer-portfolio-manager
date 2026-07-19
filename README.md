# 🚀 Developer Portfolio Manager

A command-line application built with Python that helps developers organize and manage their software projects in one place. It allows users to add, view, search, update, and delete portfolio projects while storing data persistently using JSON.

This project demonstrates clean software architecture, input validation, exception handling, unit testing, and modular Python development.

---

# 📖 Project Description

Developer Portfolio Manager is a CLI-based application designed to help developers maintain a structured portfolio of their personal and professional projects.

Instead of manually maintaining spreadsheets or notes, users can easily manage project information through an interactive command-line interface.

---

# 👥 Who is it for?

This application is useful for:

- Software Developers
- Students building a portfolio
- Freelancers managing multiple projects
- Anyone who wants to organize development projects in one place

---

# 🛠 Technologies Used

- Python 3
- JSON
- unittest
- Object-Oriented Programming (OOP)
- File Handling
- Modular Programming

---

# 🏗 Project Architecture

The project follows a layered architecture to separate responsibilities.

```
CLI Layer
      │
      ▼
Service Layer
      │
      ▼
Storage Layer
      │
      ▼
JSON File
```

### Layer Responsibilities

### CLI

- Displays menus
- Accepts user input
- Shows formatted output

### Services

- Contains business logic
- Validates operations
- Coordinates between CLI and Storage

### Storage

- Reads and writes JSON files
- Handles file operations
- Manages exception handling

### Models

- Creates project objects

### Utils

- Validation functions
- Helper methods
- UI formatting

---

# ✨ Features

✔ Add Project

✔ View Projects

✔ Search Project

✔ Update Project

✔ Delete Project

✔ Input Validation

✔ Persistent JSON Storage

✔ Exception Handling

✔ Unit Testing

✔ Clean CLI Interface

---

# 📁 Folder Structure

```
developer-portfolio-manager/
│
├── docs/
│
├── src/
│   ├── cli/
│   ├── models/
│   ├── services/
│   ├── storage/
│   └── utils/
│
├── tests/
│   └── test_project_service.py
│
├── projects.json
├── main.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/sakshi-is-commited/developer-portfolio-manager.git
```

## Navigate into the project

```bash
cd developer-portfolio-manager
```

## Run the application

```bash
python3 main.py
```

---

# 🖥 Example Menu

```
========================================
Developer Portfolio Manager
========================================

1️⃣ Add Project

2️⃣ View Projects

3️⃣ Search Project

4️⃣ Update Project

5️⃣ Delete Project

6️⃣ Exit

========================================
```

---

# 🧪 Running Unit Tests

Run all tests using:

```bash
python3 -m unittest discover tests
```

Expected output:

```
.....
----------------------------------------------------------------------
Ran 5 tests

OK
```

---

# 🛡 Exception Handling

The application gracefully handles:

- Missing JSON files
- Invalid JSON data
- Permission errors
- Invalid user input
- Unexpected runtime exceptions

---

# 🔮 Future Improvements

Potential future enhancements include:

- SQLite or PostgreSQL database support
- User authentication
- Tags and project categories
- Export portfolio to PDF
- Project statistics and analytics
- GUI version using Tkinter or PyQt
- REST API using Flask or FastAPI
- Docker support
- Cloud deployment

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Python programming
- Object-Oriented Design
- Layered Architecture
- JSON File Handling
- Exception Handling
- Input Validation
- Unit Testing using unittest
- Code Refactoring
- Clean Code Principles
- Git and GitHub workflow

---

# 📄 License

This project is created for learning and portfolio purposes.