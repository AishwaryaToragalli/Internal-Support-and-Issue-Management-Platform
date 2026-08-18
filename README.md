# Internal Support and Issue Management Platform

![Quality Checks](https://github.com/AishwaryaToragalli/Internal-Support-and-Issue-Management-Platform/github/workflows/quality.yml/badge.svg)

# Internal Support and Issue Management Platform

## Overview

A Python-based internal support platform for creating, assigning,
tracking, and resolving technical issues.

## Business Problem

Teams often manage technical issues through disconnected messages and
spreadsheets, making ownership, status, and resolution history difficult
to track.

## Features

- Ticket creation
- Ticket assignment
- Priority classification
- Status updates
- Resolution notes
- Ticket filtering
- Request validation
- Error handling
- MySQL persistence
- REST API documentation
- Automated tests
- Docker deployment
- GitHub Actions quality checks

## Technology Stack

Python, FastAPI, OOP, SQLAlchemy, MySQL, PyMySQL, Docker,
PyTest, Flake8, Git, GitHub Actions

## Local Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
docker compose up -d mysql
python -m uvicorn app.main:app --reload
```

## API Documentation

Open:

http://127.0.0.1:8000/docs

## Testing

```powershell
python -m pytest -v
python -m flake8 app tests
```

## Future Improvements

- JWT authentication
- Role-based access
- Email notifications
- SLA monitoring
- Admin dashboard
- Background task processing
- AI-powered troubleshooting search
