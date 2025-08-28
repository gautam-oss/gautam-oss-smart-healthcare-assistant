import React from 'react';
import { Link, useNavigate } from 'react-router-dom';

function Navbar() {
  const navigate = useNavigate();
  const accessToken = localStorage.getItem('access_token');
  const userType = localStorage.getItem('user_type');

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_type');
    navigate('/login');
  };

  return (
    <nav className="bg-gray-800 p-4 text-white">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold">Smart Healthcare Assistant</Link>
        <div>
          {accessToken ? (
            <>
              {userType === 'patient' && (
                <Link to="/patient-dashboard" className="mr-4">Patient Dashboard</Link>
              )}
              {userType === 'doctor' && (
                <Link to="/doctor-dashboard" className="mr-4">Doctor Dashboard</Link>
              )}
              <button onClick={handleLogout} className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded">
                Logout
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className="mr-4">Login</Link>
              <Link to="/register">Register</Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;