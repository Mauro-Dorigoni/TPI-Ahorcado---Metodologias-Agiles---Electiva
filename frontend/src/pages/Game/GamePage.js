import React from 'react';
import './GamePage.css';
import Keyboard from '../../components/keyboard/keyboard';
import Navbar from '../../components/navbar/navbar';
import Lives from '../../components/hearts/hearts';
import Word from '../../components/word/word';

function Game() {
  const currentState = ['_', 'O', '_', 'A'];

  return (
    <div className='game-page'>
      <Navbar/>
      <Word wordState={currentState} />
      <Lives lives={4} />
      <Keyboard/>
    </div>
  );
}

export default Game;
