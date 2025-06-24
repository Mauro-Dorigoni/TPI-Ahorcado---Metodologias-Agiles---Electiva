import './keyboard.css';

const Keyboard = ({ onLetterClick, usedLetters = [] }) => {
  const rows = [
    ['Q','W','E','R','T','Y','U','I','O'],
    ['P','A','S','D','F','G','H','J','K'],
    ['L','Ñ','Z','X','C','V','B','N','M']
  ];

  return (
    <div className="keyboard">
      {rows.map((row, i) => (
        <div key={i} className="keyboard-row">
          {row.map(letter => (
            <button
              key={letter}
              onClick={() => onLetterClick(letter)}
              disabled={usedLetters.includes(letter)}
              className="keyboard-button"
            >
              {letter}
            </button>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Keyboard;
