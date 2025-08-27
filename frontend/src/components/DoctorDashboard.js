import React, { useState } from 'react';
import axios from 'axios';

function DoctorDashboard() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [classificationResult, setClassificationResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setError('Please select a file first.');
      return;
    }

    setError(null);
    setClassificationResult(null);

    const formData = new FormData();
    formData.append('xray_image', selectedFile);

    try {
      const token = localStorage.getItem('access_token'); // Assuming token is stored here
      const response = await axios.post(
        'http://localhost:8000/api/reports/upload-xray/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setClassificationResult(response.data.classification);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred during upload.');
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4">Doctor Dashboard</h2>
      <div className="bg-white p-6 rounded shadow-md">
        <div className="mb-4">
          <label htmlFor="xray_upload" className="block text-gray-700 text-sm font-bold mb-2">
            Upload X-ray Image:
          </label>
          <input
            type="file"
            id="xray_upload"
            accept="image/*"
            onChange={handleFileChange}
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <button
          onClick={handleUpload}
          className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Upload and Classify X-ray
        </button>
      </div>

      {classificationResult && (
        <div className="mt-6 p-4 bg-blue-100 text-blue-800 rounded">
          <h3 className="text-lg font-semibold">Classification Result:</h3>
          <p>{classificationResult}</p>
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

export default DoctorDashboard;