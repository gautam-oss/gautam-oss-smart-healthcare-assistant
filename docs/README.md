# Smart Healthcare Assistant 🏥

## 📌 Overview
The **Smart Healthcare Assistant** is a full-stack project combining **Django REST Framework (backend)**, **TensorFlow/PyTorch (ML models)**, and **React (frontend)** to build an AI-powered healthcare platform.

## 🚀 Features
- Patient & Doctor authentication (JWT based)
- Symptom-based disease prediction (ML)
- X-ray scan classification (Normal / Pneumonia / Tumor)
- Patient history & reports stored in database
- Responsive React dashboards for Patients & Doctors

## 🛠️ Tech Stack
- **Backend**: Django REST Framework, PostgreSQL/MySQL
- **ML Models**: TensorFlow, PyTorch, Flask/FastAPI
- **Frontend**: React, Tailwind/Bootstrap
- **Deployment**: Docker, Docker Compose

## 📂 Folder Structure
```
backend/       → Django backend
ml-models/     → ML models (prediction & X-ray classification)
frontend/      → React frontend
database/      → SQL schema
```

## ⚙️ Setup Instructions
1. Clone the repo
```bash
git clone https://github.com/your-username/smart-healthcare-assistant.git
```
2. Start backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
3. Start ML model API
```bash
cd ml-models/disease_prediction
python api.py
```
4. Start frontend
```bash
cd frontend
npm install
npm start
```

## 🧠 ML Models
- **Disease Prediction** → Predicts likely disease based on symptoms.
- **X-ray Classification** → CNN model detects pneumonia/tumor from scans.

## 📊 Database Schema
- Patients, Doctors, Reports, Appointments.

## 📸 Screenshots (To be added)
- Patient Dashboard
- Doctor Dashboard
- Prediction Results

---