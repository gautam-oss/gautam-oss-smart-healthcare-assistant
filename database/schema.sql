-- Schema for Smart Healthcare Assistant

-- Table for Doctors
CREATE TABLE IF NOT EXISTS doctors_doctor (
    id SERIAL PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) UNIQUE NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20)
);

-- Table for Patients
CREATE TABLE IF NOT EXISTS patients_patient (
    id SERIAL PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login TIMESTAMP WITH TIME ZONE,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) UNIQUE NOT NULL,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined TIMESTAMP WITH TIME ZONE NOT NULL,
    date_of_birth DATE,
    phone_number VARCHAR(20)
);

-- Table for Reports
CREATE TABLE IF NOT EXISTS reports_report (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients_patient(id) ON DELETE CASCADE,
    doctor_id INTEGER REFERENCES doctors_doctor(id) ON DELETE SET NULL,
    report_type VARCHAR(100) NOT NULL,
    details TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Table for Appointments
CREATE TABLE IF NOT EXISTS reports_appointment (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients_patient(id) ON DELETE CASCADE,
    doctor_id INTEGER NOT NULL REFERENCES doctors_doctor(id) ON DELETE CASCADE,
    appointment_date TIMESTAMP WITH TIME ZONE NOT NULL,
    reason TEXT NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'scheduled',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);