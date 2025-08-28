# Smart Healthcare Assistant

This is a full-stack application designed to assist in healthcare management, featuring patient and doctor dashboards, disease prediction from symptoms, and X-ray classification.

## Project Structure

```
smart-healthcare-assistant/
├── backend/ (Django REST Framework)
├── ml-models/ (Python + FastAPI)
│   ├── disease_prediction/
│   └── xray_classification/
├── frontend/ (React + TailwindCSS)
├── database/
├── docker-compose.yml
└── README.md
```

## Technologies Used

*   **Backend:** Django REST Framework (Python)
    *   JWT Authentication
    *   PostgreSQL Database
*   **ML Models:** FastAPI (Python)
    *   Disease Prediction (from symptoms)
    *   X-ray Classification
*   **Frontend:** React.js
    *   TailwindCSS for styling
*   **Containerization:** Docker & Docker Compose

## Setup Instructions

1.  **Prerequisites:**
    *   Docker Desktop installed and running.

2.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd smart-healthcare-assistant
    ```

3.  **Build and run the Docker containers:**
    ```bash
    docker-compose up --build
    ```
    This command will:
    *   Build Docker images for the backend, frontend, and ML services.
    *   Start all services, including the PostgreSQL database.
    *   It might take a few minutes for all services to start up.

4.  **Apply Django Migrations:**
    Once the `db` and `backend` services are running, you need to apply the database migrations. Open a new terminal in the project root and run:
    ```bash
    docker-compose exec backend python backend/manage.py migrate
    ```

5.  **Create a Django Superuser (Optional but Recommended):**
    To access the Django admin panel, create a superuser:
    ```bash
    docker-compose exec backend python backend/manage.py createsuperuser
    ```
    Follow the prompts to create your superuser.

## Running the Application

*   **Frontend:** Accessible at `http://localhost:3000`
*   **Backend API:** Accessible at `http://localhost:8000`
*   **ML Disease Prediction API:** Accessible at `http://localhost:5000`
*   **ML X-ray Classification API:** Accessible at `http://localhost:5001`
*   **Django Admin:** Accessible at `http://localhost:8000/admin/`

## API Endpoints

### Authentication
*   `POST /api/patients/register/` - Register a new patient
*   `POST /api/patients/login/` - Login a patient (returns JWT tokens)
*   `POST /api/doctors/register/` - Register a new doctor
*   `POST /api/doctors/login/` - Login a doctor (returns JWT tokens)
*   `POST /api/token/refresh/` - Refresh JWT access token

### Patient Endpoints (Authentication Required)
*   `POST /api/patients/submit-symptoms/` - Submit symptoms for disease prediction

### Doctor Endpoints (Authentication Required)
*   `POST /api/doctors/upload-xray/` - Upload X-ray image for classification

## Frontend Usage

1.  **Register:** Navigate to `http://localhost:3000/register` to create a new patient or doctor account.
2.  **Login:** Use your registered credentials at `http://localhost:3000/login`.
3.  **Patient Dashboard:** After logging in as a patient, you will be redirected to the patient dashboard where you can input symptoms and get disease predictions.
4.  **Doctor Dashboard:** After logging in as a doctor, you will be redirected to the doctor dashboard where you can upload X-ray images for classification.

## Database Access

The PostgreSQL database is running in a Docker container. You can connect to it using the following details:
*   **Host:** `localhost`
*   **Port:** `5432`
*   **Database:** `postgres`
*   **User:** `postgres`
*   **Password:** `postgres`

## ML Models (Placeholder)

The `ml-models` directory contains placeholder FastAPI applications for disease prediction and X-ray classification. These models currently return dummy predictions. For a production environment, you would replace these with trained machine learning models.

*   `ml-models/disease_prediction/api.py`: Simulates disease prediction.
*   `ml-models/xray_classification/api.py`: Simulates X-ray image classification.