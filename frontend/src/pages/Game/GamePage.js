import React from 'react';
import { useState, useEffect } from 'react';
import './GamePage.css';
import Keyboard from '../../components/keyboard/keyboard';
import Navbar from '../../components/navbar/navbar';
import Lives from '../../components/hearts/hearts';
import Word from '../../components/word/word';

const apiURL = process.env.REACT_APP_API_URL;

function Game() {
  const [wordState, setWordState] = useState([]);
  const [lives, setLives] = useState(6); 
  const [usedLetters, setUsedLetters] = useState([]);
  const [rightWord, setRightWord] = useState('');

  useEffect(() => {
  setLives(6);
  setUsedLetters([]);
  //Get the righ word for debugging purposes and for popup later
  fetch(`${apiURL}/getRightWord`)
    .then(res => res.json())
    .then(data => {
      setRightWord(data.rightWord);
      //Get the current state of the users guesses
      return fetch(`${apiURL}/getWordState`);
    })
    .then(response => response.json())
    .then(data => {
      //API returns a string with dashes and/or letters, we need to split it for the letter boxes
      const wordStateArray = data.wordState.split('');
      setWordState(wordStateArray);
    })
    .catch(err => {
      console.error('Error al iniciar o cargar el juego', err);
    });
}, []);


  const handleLetterClick = (letter) => {
    const lower = letter.toLowerCase();

    // Manage the letters already used by the user
    setUsedLetters(prev => [...prev, letter]);

    // Send the guessed letter to de API
    fetch(`${apiURL}/riskedLetter?riskedLetters=${lower}`, {
      method: 'POST',
    })
      .then(res => res.json())
      .then(data => {
        const result = data.result;
        
        if (result === false) {
          // If the guess is wrong, loose a life
          setLives(prev => prev - 1);
        }

        if (result === 'Game Over') {
          alert(`¡Game Over! 😵 La palabra era: ${rightWord.toUpperCase()}`);
        }


        // Get the current word state after a guess
        return fetch(`${apiURL}/getWordState`);
      })
      .then(res => res.json())
      .then(data => {
        const wordStateArray = data.wordState.split('');
        setWordState(wordStateArray);
      })
      .catch(err => {
        console.error('Error al arriesgar letra', err);
      });
  };

  useEffect(() => {
  if (wordState.length > 0 && !wordState.includes('_')) {
    alert(`¡Ganaste! 🎉 La palabra era: ${rightWord.toUpperCase()}`);
  }
}, [wordState, rightWord]);



  return (
    <div className='game-page'>
      <Navbar/>
      <Word wordState={wordState} />
      <Lives lives={lives} />
      <Keyboard onLetterClick={handleLetterClick} usedLetters={usedLetters}/>
    </div>
  );
}

export default Game;
