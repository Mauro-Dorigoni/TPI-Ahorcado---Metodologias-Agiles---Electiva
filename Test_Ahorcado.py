import unittest
from Ahorcado_class import Ahorcado
import string
import random

class TestAhorcado(unittest.TestCase):

    #Return a random letter from the correct word
    @staticmethod
    def getRightLetter(palabra):
        letras_posibles = set(string.ascii_lowercase)
        letras_en_palabra = set(palabra.lower())
        letras_disponibles = list(letras_en_palabra)
        return random.choice(letras_disponibles)

    #Return a random letter not in the right word
    @staticmethod
    def getWrongLetter(palabra):
        letras_posibles = set(string.ascii_lowercase)
        letras_en_palabra = set(palabra.lower())
        letras_disponibles = list(letras_posibles - letras_en_palabra)
        return random.choice(letras_disponibles)

    #TEST OF RISKING WORDS
    def test_RiskWrongWordThenLose(self):
        riskedWord = "palabra"
        ahorcado = Ahorcado()
        self.assertFalse(ahorcado.riskWord(riskedWord))

    def test_RiskRightWordThenWin(self):
        ahorcado = Ahorcado()
        riskedWord = ahorcado.getRightWord()
        self.assertTrue(ahorcado.riskWord(riskedWord))
    
    #TEST OF RISKING LETTERS AND LOSE LIVES 
    #Test risking a wrong letter then lose a life
    def test_RiskWrongLetterThenLoseLife(self):
        ahorcado = Ahorcado()
        palabra = ahorcado.getRightWord()
        riskedLetter = self.getWrongLetter(palabra)
        self.assertFalse(ahorcado.riskLetter(riskedLetter))

    def test_RiskRightLetterThenKeepLife(self):
        ahorcado = Ahorcado()
        palabra = ahorcado.getRightWord()
        riskedLetter = self.getRightLetter(palabra)
        self.assertTrue(ahorcado.riskLetter(riskedLetter))

    def test_RiskSixWrongLettersThenLoseGame(self):
        ahorcado = Ahorcado()
        palabra = ahorcado.getRightWord()
    
        wrongLetters = list(set(string.ascii_lowercase) - set(palabra))
        riskedLetters = wrongLetters[:6]

        for i in range(5):
            ahorcado.riskLetter(riskedLetters[i])
    
        self.assertEqual(ahorcado.riskLetter(riskedLetters[5]), "Game Over")
    
    #Test that the right word is a string and not empty
    def test_getRightWord(self):
        ahorcado = Ahorcado()
        rightWord = ahorcado.getRightWord()
        self.assertIsInstance(rightWord,str)
        self.assertTrue(rightWord.strip() != "") 
    
    #Test that the right word is not empty
    def test_NotReceiveWord(self):
        ahorcado = Ahorcado()
        rightWord = ahorcado.getRightWord()
        self.assertTrue(rightWord.strip() != "")

    #Test that the word is diferent in five instances of Ahorcado
    def test_FiveDifferentWords(self):
        ahorcado1 = Ahorcado()
        ahorcado2 = Ahorcado()
        ahorcado3 = Ahorcado()
        ahorcado4 = Ahorcado()
        ahorcado5 = Ahorcado()
        
        words = {
        ahorcado1.getRightWord(),
        ahorcado2.getRightWord(),
        ahorcado3.getRightWord(),
        ahorcado4.getRightWord(),
        ahorcado5.getRightWord(),
        }

        self.assertEqual(len(words), 5)

    #Test that the player has 6 lives at the start of the game
    def test_startLives6(self):
        ahorcado = Ahorcado()
        self.assertEqual(ahorcado.lives, 6)
    
    #Test that initially the word is hidden (by showing a _ for each letter)
    def test_InitialWordHidden(self):
        ahorcado = Ahorcado()
        palabra = ahorcado.getRightWord()
        estado = ahorcado.getWordState()
        for letra in estado:
            self.assertEqual(letra, '_')
        self.assertEqual(len(estado), len(palabra))

    #Test that at the beginning there are no risked letters
    def test_InitialRiskedLettersEmpty(self):
        ahorcado = Ahorcado()
        self.assertEqual(len(ahorcado.getRiskedLetters()), 0)

    def test_RiskWrongLetterAgainNotLoseLife(self):
        ahorcado = Ahorcado()
        palabra = ahorcado.getRightWord()
        riskedLetter = self.getWrongLetter(palabra)

        risk1 = ahorcado.riskLetter(riskedLetter)
        lives1 = ahorcado.lives

        risk2 = ahorcado.riskLetter(riskedLetter)
        lives2 = ahorcado.lives

        self.assertEqual(lives1, lives2)

if __name__ == '__main__':
    unittest.main()