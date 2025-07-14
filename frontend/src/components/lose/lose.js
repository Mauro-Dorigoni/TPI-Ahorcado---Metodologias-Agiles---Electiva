import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './lose.css';

const Lose = ({ word, time }) => {
  const navigate = useNavigate();

  const formatTime = (seconds) => {
    const mins = String(Math.floor(seconds / 60)).padStart(2, '0');
    const secs = String(seconds % 60).padStart(2, '0');
    return `${mins}:${secs}`;
  };

  useEffect(() => {
    const handleClickOutside = (e) => {
      if (e.target.classList.contains('win-overlay')) {
        navigate('/');
      }
    };
    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  }, [navigate]);

  return (
    <div className="lose-overlay">
      <div className="lose-popup">
        <button className="close-button" onClick={() => navigate('/')}>〈 </button>
        <h1>GAME OVER</h1>
        <p>The stick figure didn't make it... but don't give up! Try again and beat the game!</p>
        <div className="win-columns">
          <div className="win-column">
            <h6>The word was:</h6>
            <p data-testid="correct-word"><strong>{word.toUpperCase()}</strong></p>
          </div>
          <div className="win-column">
            <h6>Time:</h6>
            <p className="time"><strong>{formatTime(time)}</strong></p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Lose;
