# 🚀 Developer Portfolio Manager

> A professional Command Line Interface (CLI) application built with Python for managing and organizing software development projects.

---

# 📖 Project Overview

Developer Portfolio Manager is a Python-based CLI application that enables developers to maintain a structured portfolio of their personal and professional projects.

The application allows users to add, view, search, update, and delete project information while storing data persistently using a JSON file.

Built using a layered architecture, the project demonstrates clean code practices, modular design, exception handling, and unit testing.

---

# ❓ Problem Statement

Developers often manage multiple projects across different technologies and repositories.

Keeping track of project details such as:

- Project Name
- Description
- Technology Stack
- GitHub Repository
- Project Status

using spreadsheets or text files quickly becomes unorganized and difficult to maintain.

There was a need for a lightweight, easy-to-use application that could efficiently manage a developer's portfolio from the command line.

---

# 💡 Solution

Developer Portfolio Manager provides a simple interactive CLI that allows users to:

- Store project information
- Search projects instantly
- Update existing projects
- Delete obsolete projects
- Persist data locally using JSON

The application follows a layered architecture, separating presentation, business logic, and data storage, making it easy to maintain and extend.

---

# ✨ Features

## Project Management

- ✅ Add Project
- ✅ View Projects
- ✅ Search Projects
- ✅ Update Projects
- ✅ Delete Projects

---

## Data Management

- ✅ Persistent JSON Storage
- ✅ Automatic JSON File Creation
- ✅ Input Validation
- ✅ Search (Case-Insensitive & Partial Match)

---

## User Experience

- ✅ Clean CLI Interface
- ✅ Formatted Output
- ✅ Success, Warning & Error Messages
- ✅ Reusable Helper Functions

---

## Reliability

- ✅ Exception Handling
- ✅ Missing File Recovery
- ✅ Invalid JSON Handling
- ✅ Permission Error Handling
- ✅ Unexpected Exception Handling

---

## Testing

- ✅ Unit Testing using Python unittest
- ✅ Add Project Test
- ✅ Search Project Test
- ✅ Update Project Test
- ✅ Delete Project Test

---

# 🏗 Architecture

The application follows a layered architecture.

```text
               +----------------------+
               |     CLI Layer        |
               |  (User Interface)    |
               +----------+-----------+
                          |
                          ▼
               +----------------------+
               |   Service Layer      |
               | (Business Logic)     |
               +----------+-----------+
                          |
                          ▼
               +----------------------+
               |   Storage Layer      |
               | (JSON File Access)   |
               +----------+-----------+
                          |
                          ▼
               +----------------------+
               |     projects.json    |
               |   Persistent Data    |
               +----------------------+
```

### Layer Responsibilities

### CLI

- Displays menus
- Takes user input
- Formats output

### Services

- Implements business logic
- Coordinates application flow
- Validates operations

### Storage

- Reads and writes project data
- Handles file operations
- Performs exception handling

### Models

- Creates project objects

### Utils

- Input validation
- Helper functions
- UI formatting

---

# 📁 Folder Structure

```text
developer-portfolio-manager/
│
├── docs/
│   └── PROJECT_SHOWCASE.md
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

# 🛠 Technologies Used

- Python 3
- JSON
- unittest
- Object-Oriented Programming (OOP)
- File Handling
- Modular Programming

---

# 🧪 Testing

The project includes automated unit tests for the core business logic.

### Tests Covered

- Add Project
- Search Existing Project
- Search Missing Project
- Update Project
- Delete Project

Run the tests using:

```bash
python3 -m unittest discover tests
```

Expected Output:

```text
.....
----------------------------------------------------------------------
Ran 5 tests

OK
```

---

# 🛡 Exception Handling

The application gracefully handles common runtime errors including:

- Missing JSON file
- Corrupted JSON data
- Permission denied errors
- Invalid user input
- Unexpected exceptions

Instead of crashing, the application displays clear, user-friendly messages and continues running whenever possible.

---

# 🔮 Future Improvements

Potential enhancements for future versions include:

### Database Support

- SQLite
- PostgreSQL
- MySQL

### Backend API

- Flask REST API
- FastAPI

### User Interface

- Web Interface
- Desktop GUI (Tkinter or PyQt)
- Dark Theme
- Responsive Dashboard

### Authentication

- User Login
- Role-Based Access
- Secure Password Hashing

### Export & Reporting

- CSV Export
- PDF Portfolio Export
- Excel Export

### Additional Features

- Project Categories
- Tags & Filtering
- Project Analytics
- Progress Tracking
- Search by Technology
- Backup & Restore

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Python Programming
- Object-Oriented Design
- Layered Architecture
- JSON Data Storage
- Exception Handling
- Input Validation
- Unit Testing
- Code Refactoring
- Clean Code Principles
- Git & GitHub Workflow

---

# 🎯 Conclusion

Developer Portfolio Manager is a portfolio-ready Python application that demonstrates software engineering best practices through clean architecture, modular design, comprehensive testing, and robust exception handling.

The project serves as a strong foundation for future enhancements such as database integration, REST APIs, authentication, and web-based interfaces, making it a scalable and maintainable solution for managing developer portfolios.