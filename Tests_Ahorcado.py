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


    def test_RiskWrongWordThenLose(self):
        riskedWord = "palabra"
        ahorcado = Ahorcado()
        self.assertFalse(ahorcado.riskWord(riskedWord))

    def test_RiskRightWordThenWin(self):
        ahorcado = Ahorcado()
        riskedWord = ahorcado.getRightWord()
        self.assertTrue(ahorcado.riskWord(riskedWord))
    
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
        riskedLetters = [self.getWrongLetter(palabra),self.getWrongLetter(palabra),self.getWrongLetter(palabra),self.getWrongLetter(palabra),self.getWrongLetter(palabra),self.getWrongLetter(palabra)]
        for i in range(0,5,1):
            ahorcado.riskLetter(riskedLetters[i])
        self.assertEqual(ahorcado.riskLetter(riskedLetters[5]),"Game Over")

    def test_getRightWord(self):
        ahorcado = Ahorcado()
        rightWord = ahorcado.getRightWord()
        self.assertIsInstance(rightWord,str)
        self.assertTrue(rightWord.strip() != "") 

    def test_NotReceiveWord(self):
        ahorcado = Ahorcado()
        rightWord = ahorcado.getRightWord()
        self.assertTrue(rightWord.strip() != "")

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

if __name__ == '__main__':
    unittest.main()