import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // We will create this file for Tailwind CSS imports
import App from './App';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);