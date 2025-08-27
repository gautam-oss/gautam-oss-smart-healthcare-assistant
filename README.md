# Smart Healthcare Assistant

This is a full-stack application for a Smart Healthcare Assistant, built with Django REST Framework for the backend, FastAPI for ML models, React for the frontend, and PostgreSQL as the database. Docker is used for containerization.

## Project Structure

- `backend/`: Django REST Framework application.
- `ml-models/`: FastAPI applications for disease prediction and X-ray classification.
- `frontend/`: React application.
- `database/`: Contains the PostgreSQL schema.
- `docker-compose.yml`: Defines and links all services.

## Setup and Running

1.  **Prerequisites:**
    - Docker and Docker Compose installed.

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
    - Build Docker images for the backend, ML models, and frontend.
    - Start all services (PostgreSQL database, Django backend, ML APIs, React frontend).

4.  **Apply Django Migrations:**
    Once the containers are up, you need to apply Django migrations to create the database tables.
    Open a new terminal and run:
    ```bash
    docker-compose exec backend python manage.py makemigrations
    docker-compose exec backend python manage.py migrate
    ```

5.  **Create a Django Superuser (Optional, for Admin Panel access):**
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```
    Follow the prompts to create a superuser.

6.  **Access the Application:**
    - **Frontend (React):** Open your browser and go to `http://localhost:3000`
    - **Backend (Django REST Framework):** API endpoints are available at `http://localhost:8000/api/`
    - **ML Disease Prediction API:** `http://localhost:8001/predict`
    - **ML X-ray Classification API:** `http://localhost:8002/classify`
    - **Django Admin:** `http://localhost:8000/admin/`

## Usage

- **Register:** Create new patient or doctor accounts via the frontend.
- **Login:** Log in as a patient or doctor.
- **Patient Dashboard:** Submit symptoms to get disease predictions.
- **Doctor Dashboard:** Upload X-ray images for classification.

## Stopping the Application

To stop all running containers, press `Ctrl+C` in the terminal where `docker-compose up` is running. To remove the containers and networks, run:

```bash
docker-compose down
```

To remove volumes (which will delete your database data), add the `-v` flag:

```bash
docker-compose down -v
```
