import React from 'react';
import './word.css';

const Word = ({ wordState }) => {
  return (
    <div className="word-container">
      {wordState.map((letter, index) => (
        <div key={index} className="letter-box">
          {letter.toUpperCase()}
        </div>
      ))}
    </div>
  );
};

export default Word;
