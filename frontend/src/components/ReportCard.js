import React from 'react';

function ReportCard({ report }) {
  return (
    <div className="bg-white shadow-md rounded-lg p-4 mb-4">
      <h3 className="text-xl font-semibold text-gray-800">Report Type: {report.report_type}</h3>
      <p className="text-gray-600">Patient: {report.patient_username}</p>
      {report.doctor_username && <p className="text-gray-600">Doctor: {report.doctor_username}</p>}
      <p className="text-gray-700 mt-2">Details: {report.details}</p>
      <p className="text-gray-500 text-sm mt-2">Created At: {new Date(report.created_at).toLocaleString()}</p>
    </div>
  );
}

export default ReportCard;