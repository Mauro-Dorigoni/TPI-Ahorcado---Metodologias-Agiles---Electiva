import React, { useState, useEffect } from 'react';
import './guess.css';

const Guess = ({ onClose, onSubmit, wordLength = 1 }) => {
  const [guess, setGuess] = useState('');

  const handleKeyClick = (letter) => {
    if (guess.length < wordLength) {
      setGuess(prev => prev + letter);
    }
  };

  const handleDelete = () => {
    setGuess(prev => prev.slice(0, -1));
  };

  const handleSubmit = () => {
    if (guess.length > 0) {
      onSubmit(guess.toLowerCase());
      setGuess('');
      onClose();
    }
  };

  useEffect(() => {
    const handleOutsideClick = (e) => {
      if (e.target.classList.contains('guess-overlay')) {
        onClose();
      }
    };
    document.addEventListener('click', handleOutsideClick);
    return () => document.removeEventListener('click', handleOutsideClick);
  }, [onClose]);

  const rows = [
    ['Q','W','E','R','T','Y','U','I','O'],
    ['P','A','S','D','F','G','H','J','K'],
    ['L','Ñ','Z','X','C','V','B','N','M']
  ];

  return (
    <div className="guess-overlay">
      <div className="guess-popup">
        <button className="close-button" onClick={onClose}>〈</button>
        <h2>Guess the word</h2>

        <div className="guess-boxes">
          {[...Array(wordLength)].map((_, i) => (
            <div key={i} className="guess-letter">{guess[i]?.toUpperCase() || ''}</div>
          ))}
        </div>

        <div className="guess-keyboard">
          {rows.map((row, i) => (
            <div key={i} className="guess-keyboard-row">
              {row.map(letter => (
                <button key={letter} className="guess-keyboard-button" onClick={() => handleKeyClick(letter)}>
                  {letter}
                </button>
              ))}
            </div>
          ))}
          <div className="guess-keyboard-row action-row">
            <button className="guess-keyboard-button action-button" onClick={handleDelete}>🡠</button>
            <button className="guess-keyboard-button action-button" onClick={handleSubmit} data-testid="check">✓</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Guess;
