import React, { useContext } from 'react';
import './navbar.css';
import time from '../../media/time.png';
import { GameContext } from '../../context/GameContext';

const Navbar = () => {
  const { formatTime } = useContext(GameContext);

  return (
    <div className='navbar-container'>
      <div className='time-container'>
        <img src={time} alt='Time Icon' className='time-icon' />
        <h2 className='timer-text'>{formatTime()}</h2>
      </div>
      <div className='exit-container'>
        <button className='exit-button'>Exit</button>
      </div>
    </div>
  );
};

export default Navbar;
