import React, { useState, useEffect, useContext } from 'react';
import './GamePage.css';
import Keyboard from '../../components/keyboard/keyboard';
import Navbar from '../../components/navbar/navbar';
import Lives from '../../components/hearts/hearts';
import Word from '../../components/word/word';
import Win from '../../components/win/win';
import Lose from '../../components/lose/lose';
import Guess from '../../components/guess/guess';
import { GameContext } from '../../context/GameContext';

const apiURL = process.env.REACT_APP_API_URL;

function Game() {
  const [wordState, setWordState] = useState([]);
  const [lives, setLives] = useState(6);
  const [usedLetters, setUsedLetters] = useState([]);
  const [rightWord, setRightWord] = useState('');
  const [correctLetter, setCorrectLetter] = useState(null);
  const [showWin, setShowWin] = useState(false);
  const [showLose, setShowLose] = useState(false);
  const [showGuessPopup, setShowGuessPopup] = useState(false);
  const { time, stopTimer } = useContext(GameContext);

  useEffect(() => {
    setLives(6);
    setUsedLetters([]);

    fetch(`${apiURL}/getRightWord`,{credentials:"include"})
      .then(res => res.json())
      .then(data => {
        setRightWord(data.rightWord);
        return fetch(`${apiURL}/getWordState`,{credentials:"include"});
      })
      .then(res => res.json())
      .then(data => {
        const wordStateArray = data.wordState.split('');
        setWordState(wordStateArray);
      })
      .catch(err => {
        console.error('Error al iniciar o cargar el juego', err);
      });
  }, []);

  const handleLetterClick = (letter) => {
    const lower = letter.toLowerCase();
    setUsedLetters(prev => [...prev, letter]);

    fetch(`${apiURL}/riskedLetter?riskedLetters=${lower}`, {
      method: 'POST',
      credentials: "include",
    })
      .then(res => res.json())
      .then(data => {
        const result = data.result;

        if (result === true) {
          setCorrectLetter(letter);
          setTimeout(() => setCorrectLetter(null), 1000);
        }

        if (result === false) {
          setLives(prev => prev - 1);
        }

        if (result === 'Game Over') {
          stopTimer();
          setShowLose(true);
        }

        return fetch(`${apiURL}/getWordState`,{credentials:"include"});
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

  const handleGuessSubmit = (guess) => {
    const formattedGuess = guess.trim().toLowerCase();
    setShowGuessPopup(false);
    if (formattedGuess === rightWord.toLowerCase()) {
      stopTimer();
      setShowWin(true);
    } else {
      stopTimer();
      setShowLose(true);
    }
  };

  useEffect(() => {
    if (wordState.length > 0 && !wordState.includes('_')) {
      stopTimer();
      setShowWin(true);
    }
  }, [wordState, rightWord, stopTimer]);

  return (
    <div className='game-page'>
      <Navbar />
      <Word wordState={wordState} correctLetter={correctLetter} />
      <Lives lives={lives} />
      <Keyboard
        onLetterClick={handleLetterClick}
        usedLetters={usedLetters}
        correctLetter={correctLetter}
      />

      <button className="guess-button" onClick={() => setShowGuessPopup(true)}>
        Guess
      </button>

      {showGuessPopup && (
        <Guess
          onClose={() => setShowGuessPopup(false)}
          onSubmit={handleGuessSubmit}
          wordLength={rightWord.length}
        />
      )}

      {showWin && <Win word={rightWord} time={time} />}
      {showLose && <Lose word={rightWord} time={time} />}
    </div>
  );
}

export default Game;
