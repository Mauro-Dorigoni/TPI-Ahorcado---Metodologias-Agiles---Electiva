import React, { useContext, useState } from 'react';
import './navbar.css';
import time from '../../media/time.png';
import { GameContext } from '../../context/GameContext';
import ConfirmExit from '../../components/exit/exit';

const Navbar = () => {
  const { formatTime } = useContext(GameContext);
  const [showConfirm, setShowConfirm] = useState(false);

  const handleExitClick = () => {
    setShowConfirm(true);
  };

  const handleCancel = () => {
    setShowConfirm(false);
  };

  return (
    <>
      <div className='navbar-container'>
        <div className='time-container'>
          <img src={time} alt='Time Icon' className='time-icon' />
          <h2 className='timer-text'>{formatTime()}</h2>
        </div>
        <div className='exit-container'>
          <button className='exit-button' onClick={handleExitClick}>Exit</button>
        </div>
      </div>
      {showConfirm && <ConfirmExit onCancel={handleCancel} />}
    </>
  );
};

export default Navbar;
