# Student Management System

A web-based student management application developed for the CI/CD assignment with GitHub Actions. It includes user authentication, dashboard analytics, and student record management with automated Selenium testing.

Live Demo: https://sadiarahman30.github.io/StudentManagementSystem/

## Features

- Login and registration with localStorage persistence
- Student dashboard with total counts and department statistics
- Add, edit, and delete student records
- Search by name, ID, or email, and filter by department or status
- Export student list to CSV
- Light and dark theme toggle

## Project Structure

- index.html - Login page
- register.html - Registration page
- dashboard.html - Student dashboard
- css/style.css - Stylesheet
- tests/ - Selenium automated tests
- run_tests.py - Script to run all tests
- .github/workflows/ci-cd.yml - GitHub Actions CI/CD workflow

## Running Locally

Open index.html in any browser, or run a local server:

```bash
python3 -m http.server 8000
```

Default credentials:
- Email: admin@sms.com
- Password: admin123

## Running Tests

Install requirements:
```bash
pip install -r requirements.txt
```

Run test suite:
```bash
python3 run_tests.py
```

## CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment:
1. CI: On every push to main, an Ubuntu runner installs dependencies and executes run_tests.py using headless Chrome.
2. CD: If all tests pass, the repository is automatically deployed to GitHub Pages.
