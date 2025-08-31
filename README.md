# Docker Sample Project
# Dockerized Voting App

# 🗳️ Docker Voting App (Frontend + Backend + Redis)

A simple voting application built with **Flask (Backend)**, **HTML/JS (Frontend)**, and **Redis (Database)**.  
Deployed using **Docker Compose** with three services: `frontend`, `backend`, and `redis`.

---

## 🚀Features
- Vote between **Cats** and **Dogs** 🐱
- votes are stored in **Redis**
- Results page shows live vote counts
- Frontend communicates with backend API through Docker network
- CORS enabled to allow frontend-backend communication

---

## project Structure
.
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── index.html
│ └── Dockerfile
├── docker-compose.yml
└── README.md
Setup & Run

### Clone Repository

git clone https://github.com/vigneshmv14398/Docker-sample-project
cd Docker-sample-project

# Build and Run
docker-compose up --build

# Access the App

Frontend: http://localhost:8080

Backend API: http://localhost:5000

/vote → Cast a vote

/results → View results
