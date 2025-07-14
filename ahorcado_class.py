"""
Módulo que implementa la lógica del juego Ahorcado.
"""
import random
import string


class Ahorcado:
    """Clase que representa la lógica del juego Ahorcado."""

    possibleLetters = set(string.ascii_lowercase)  # Constante de clase

    def __init__(self, testMode):
        if testMode:
            self.rightWord = 'python'
        else:
            self.rightWord = self._getWord()
        self.lives = 6
        self.wordState = ['_' for _ in self.rightWord]
        self.riskedLetters = set()
        

    def getWordState(self):
        """Devuelve el estado actual de la palabra con letras descubiertas."""
        return ''.join(self.wordState)

    def getRightWord(self):
        """Devuelve la palabra correcta."""
        return self.rightWord

    def riskWord(self, riskedWord: str):
        """Verifica si la palabra arriesgada es correcta."""
        return riskedWord == self.rightWord

    def riskLetter(self, riskedLetter: str):
        """
        Procesa una letra arriesgada.
        Retorna True si la letra está en la palabra,
        actualiza el estado visible de la palabra,
        resta una vida y retorna False si no está,
        y retorna "Game Over" si se acaban las vidas.
        """
        riskedLetter = riskedLetter.lower()

        if riskedLetter in self.riskedLetters:
            return False

        self.riskedLetters.add(riskedLetter)

        if riskedLetter in self.rightWord:
            for idx, char in enumerate(self.rightWord):
                if char == riskedLetter:
                    self.wordState[idx] = riskedLetter
            return True
        self.lives -= 1
        if self.lives == 0:
            return "Game Over"
        return False

    def getRiskedLetters(self):
        """Devuelve el conjunto de letras arriesgadas."""
        return self.riskedLetters

    def _getWord(self):
        """Selecciona una palabra aleatoria desde el archivo 'palabras.txt'."""
        with open('palabras.txt', 'r', encoding='utf-8') as f:
            palabras = [line.strip() for line in f if line.strip()]
            return random.choice(palabras).lower()
