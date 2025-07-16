"""
Módulo con tests para la clase Ahorcado.
"""

import string
import random
import unittest
from ahorcado_class import Ahorcado


class TestAhorcado(unittest.TestCase):
    """Tests para la clase Ahorcado."""

    @staticmethod
    def getRightLetter(palabra):
        """Devuelve una letra aleatoria que está en la palabra."""
        #letrasPosibles = set(string.ascii_lowercase)
        letrasEnPalabra = set(palabra.lower())
        letrasDisponibles = list(letrasEnPalabra)
        return random.choice(letrasDisponibles)

    @staticmethod
    def getWrongLetter(palabra):
        """Devuelve una letra aleatoria que no está en la palabra."""
        letrasPosibles = set(string.ascii_lowercase)
        letrasEnPalabra = set(palabra.lower())
        letrasDisponibles = list(letrasPosibles - letrasEnPalabra)
        return random.choice(letrasDisponibles)

    def testRiskWrongWordThenLose(self):
        """Prueba que arriesgar una palabra incorrecta retorna False."""
        riskedWord = "palabra"
        ahorcado = Ahorcado(False)
        self.assertFalse(ahorcado.riskWord(riskedWord))

    def testRiskRightWordThenWin(self):
        """Prueba que arriesgar la palabra correcta retorna True."""
        ahorcado = Ahorcado(False)
        riskedWord = ahorcado.getRightWord()
        self.assertTrue(ahorcado.riskWord(riskedWord))

    def testRiskWrongLetterThenLoseLife(self):
        """Prueba que arriesgar una letra incorrecta resta una vida."""
        ahorcado = Ahorcado(False)
        palabra = ahorcado.getRightWord()
        riskedLetter = self.getWrongLetter(palabra)
        self.assertFalse(ahorcado.riskLetter(riskedLetter))

    def testRiskRightLetterThenKeepLife(self):
        """Prueba que arriesgar una letra correcta no resta vidas."""
        ahorcado = Ahorcado(False)
        palabra = ahorcado.getRightWord()
        riskedLetter = self.getRightLetter(palabra)
        self.assertTrue(ahorcado.riskLetter(riskedLetter))

    def testRiskSixWrongLettersThenLoseGame(self):
        """Prueba que arriesgar seis letras incorrectas termina el juego."""
        ahorcado = Ahorcado(False)
        palabra = ahorcado.getRightWord()
        wrongLetters = list(set(string.ascii_lowercase) - set(palabra))
        riskedLetters = wrongLetters[:6]

        for i in range(5):
            ahorcado.riskLetter(riskedLetters[i])

        self.assertEqual(ahorcado.riskLetter(riskedLetters[5]), "Game Over")

    def testGetRightWord(self):
        """Prueba que la palabra correcta es una cadena no vacía."""
        ahorcado = Ahorcado(False)
        rightWord = ahorcado.getRightWord()
        self.assertIsInstance(rightWord, str)
        self.assertTrue(rightWord.strip() != "")

    def testNotReceiveWord(self):
        """Prueba que la palabra correcta no está vacía."""
        ahorcado = Ahorcado(False)
        rightWord = ahorcado.getRightWord()
        self.assertTrue(rightWord.strip() != "")

    def testFiveDifferentWords(self):
        """Prueba que cinco instancias tienen palabras diferentes."""
        ahorcado1 = Ahorcado(False)
        ahorcado2 = Ahorcado(False)
        ahorcado3 = Ahorcado(False)
        ahorcado4 = Ahorcado(False)
        ahorcado5 = Ahorcado(False)

        words = {
            ahorcado1.getRightWord(),
            ahorcado2.getRightWord(),
            ahorcado3.getRightWord(),
            ahorcado4.getRightWord(),
            ahorcado5.getRightWord(),
        }

        self.assertEqual(len(words), 5)

    def testStartLives6(self):
        """Prueba que el jugador inicia con 6 vidas."""
        ahorcado = Ahorcado(False)
        self.assertEqual(ahorcado.lives, 6)

    def testInitialWordHidden(self):
        """Prueba que la palabra inicial está oculta con guiones bajos."""
        ahorcado = Ahorcado(False)
        palabra = ahorcado.getRightWord()
        estado = ahorcado.getWordState()
        for letra in estado:
            self.assertEqual(letra, '_')
        self.assertEqual(len(estado), len(palabra))

    def testInitialRiskedLettersEmpty(self):
        """Prueba que inicialmente no hay letras arriesgadas."""
        ahorcado = Ahorcado(False)
        self.assertEqual(len(ahorcado.getRiskedLetters()), 0)

    def testRiskWrongLetterAgainNotLoseLife(self):
        """Prueba que arriesgar la misma letra incorrecta no resta vidas adicionales."""
        ahorcado = Ahorcado(False)
        palabra = ahorcado.getRightWord()
        riskedLetter = self.getWrongLetter(palabra)

        ahorcado.riskLetter(riskedLetter)
        lives1 = ahorcado.lives

        ahorcado.riskLetter(riskedLetter)
        lives2 = ahorcado.lives

        self.assertEqual(lives1, lives2)


# if __name__ == '__main__':
#     unittest.main()
