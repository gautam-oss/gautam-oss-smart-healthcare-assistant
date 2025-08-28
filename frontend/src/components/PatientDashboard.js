import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function PatientDashboard() {
  const [symptoms, setSymptoms] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      navigate('/login');
    }
  }, [navigate]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setPrediction(null);

    try {
      const token = localStorage.getItem('access_token'); // Assuming token is stored here
      const response = await axios.post(
        'http://localhost:8000/api/patients/submit-symptoms/',
        { symptoms },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setPrediction(response.data.prediction);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Patient Dashboard</h2>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md">
        <div className="mb-4">
          <label htmlFor="symptoms" className="block text-gray-700 text-sm font-bold mb-2">
            Enter Symptoms:
          </label>
          <textarea
            id="symptoms"
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            rows="5"
            value={symptoms}
            onChange={(e) => setSymptoms(e.target.value)}
            required
          ></textarea>
        </div>
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Get Disease Prediction
        </button>
      </form>

      {prediction && (
        <div className="mt-6 p-4 bg-green-100 text-green-800 rounded">
          <h3 className="text-lg font-semibold">Prediction Result:</h3>
          <p>{prediction}</p>
        </div>
      )}

      {error && (
        <div className="mt-6 p-4 bg-red-100 text-red-800 rounded">
          <h3 className="text-lg font-semibold">Error:</h3>
          <p>{error}</p>
        </div>
      )}
    </div>
  );
}

export default PatientDashboard;