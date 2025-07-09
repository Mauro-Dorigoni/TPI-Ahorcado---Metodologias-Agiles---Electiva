import React from 'react';
import { useNavigate } from 'react-router-dom';
import './exit.css';

const ConfirmExit = ({ onCancel }) => {
  const navigate = useNavigate();

  return (
    <div className="exit-overlay">
      <div className="exit-popup">
        <h1>Are you sure you want to exit?</h1>
        <p>If you exit, your current progress will be lost.</p>
        <div style={{ marginTop: '30px' }}>
          <button 
            style={{ marginRight: '20px' }} 
            onClick={() => navigate('/')}
            className="confirm-button"
          >
            Yes
          </button>
          <button onClick={onCancel} className="cancel-button">No</button>
        </div>
      </div>
    </div>
  );
};

export default ConfirmExit;
