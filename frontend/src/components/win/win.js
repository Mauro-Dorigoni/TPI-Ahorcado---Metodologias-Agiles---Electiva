import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './win.css';

const Win = ({ word, time }) => {
  const navigate = useNavigate();

  // Función para formatear el tiempo recibido (en segundos)
  const formatTime = (seconds) => {
    const mins = String(Math.floor(seconds / 60)).padStart(2, '0');
    const secs = String(seconds % 60).padStart(2, '0');
    return `${mins}:${secs}`;
  };

  // Cierra al hacer click fuera del popup
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
    <div className="win-overlay">
      <div className="win-popup">
        <button className="close-button" onClick={() => navigate('/')}>〈 </button>
        <h1>CONGRATS!</h1>
        <p>You cracked the code, saved the stick figure, and proved your word-guessing powers! Thanks for playing — you're officially a Hangman Hero.</p>
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

export default Win;
