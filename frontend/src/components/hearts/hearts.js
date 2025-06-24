import React from 'react';
import './hearts.css';
import filledHeart from '../../media/filled-heart.png';
import emptyHeart from '../../media/empty-heart.png';

const Lives = ({ lives }) => {
  const totalLives = 6;

  return (
    <div className="lives-container">
      {Array.from({ length: totalLives }, (_, i) => (
        <img
          key={i}
          src={i < lives ? filledHeart : emptyHeart}
          alt={i < lives ? 'Filled Heart' : 'Empty Heart'}
          className="heart-icon"
        />
      ))}
    </div>
  );
};

export default Lives;
