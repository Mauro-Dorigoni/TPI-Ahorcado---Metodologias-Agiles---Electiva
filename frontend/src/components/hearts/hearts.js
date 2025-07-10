import React, { useEffect, useRef, useState } from 'react';
import './hearts.css';
import filledHeart from '../../media/filled-heart.png';
import emptyHeart from '../../media/empty-heart.png';

const Lives = ({ lives }) => {
  const totalLives = 6;
  const [shakingIndex, setShakingIndex] = useState(null);
  const prevLivesRef = useRef(lives);

  useEffect(() => {
    const prevLives = prevLivesRef.current;
    if (lives < prevLives) {
      // Se perdió exactamente una vida, marcamos cuál
      setShakingIndex(lives); // el índice de la vida perdida
      setTimeout(() => setShakingIndex(null), 400); // quitamos la animación
    }
    prevLivesRef.current = lives;
  }, [lives]);

  return (
    <div className="lives-container">
      {Array.from({ length: totalLives }, (_, i) => (
        <img
          key={i}
          src={i < lives ? filledHeart : emptyHeart}
          alt={i < lives ? 'Filled Heart' : 'Empty Heart'}
          className={`heart-icon ${i === shakingIndex ? 'heart-lost' : ''}`}
        />
      ))}
    </div>
  );
};

export default Lives;
