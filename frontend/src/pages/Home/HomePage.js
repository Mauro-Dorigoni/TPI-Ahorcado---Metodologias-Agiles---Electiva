import React from 'react';
import './HomePage.css';
import logo from '../../media/logo.png';
import { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { GameContext } from '../../context/GameContext';

const apiURL = process.env.REACT_APP_API_URL;


const Home = () => {
  const navigate = useNavigate();
  const { startTimer } = useContext(GameContext);

  const handleStart = (e) => {
    fetch(`${apiURL}/startGame`,{method: "POST"});
    e.preventDefault();
    startTimer();
    navigate("/game");
  };

  return (
    <div className='home-page'>
      <div className='logo-container'>
        <img src={logo} alt='Group Logo' className='logo'/>
      </div>

      <form className='game-form'>
        <h2>Select Lenguage</h2>
        <select id='language' name='language'>
          <option value='english'>English</option>
          <option value='spanish'>Spanish</option>
        </select>

        <h2>Select Difficulty</h2>
        <select id='difficulty' name='difficulty'>
          <option value='easy'>Easy</option>
          <option value='medium'>Medium</option>
          <option value='hard'>Hard</option>
        </select>

        <button type="button" onClick={handleStart} className='start-button'>Start Game</button>
      </form>
    </div>
  );
}

export default Home;
