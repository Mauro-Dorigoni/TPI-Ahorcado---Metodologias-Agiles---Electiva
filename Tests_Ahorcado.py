import unittest
from Ahorcado_class import Ahorcado


class TestAhorcado(unittest.TestCase):

    """ def test_RiskWrongWordThenLose(self):
        riskedWord = "palabra"
        ahorcado = Ahorcado("hola")
        self.assertFalse(ahorcado.riskWord(riskedWord))

    def test_RiskRightWordThenWin(self):
        riskedWord = "Universidad"
        ahorcado = Ahorcado(riskedWord)
        self.assertTrue(ahorcado.riskWord(riskedWord))
    
    def test_RiskWrongLetterThenLoseLife(self):
        riskedLetter = 'k'
        ahorcado = Ahorcado("Universidad")
        self.assertFalse(ahorcado.riskLetter(riskedLetter))

    def test_RiskRightLetterThenKeepLife(self):
        riskedLetter = 'U'
        ahorcado = Ahorcado("Universidad")
        self.assertTrue(ahorcado.riskLetter(riskedLetter))

    def test_RiskRightLetterThenKeepLife_v2(self):
        riskedLetter = 'd'
        ahorcado = Ahorcado("Universidad")
        self.assertTrue(ahorcado.riskLetter(riskedLetter))

    def test_RiskSixWrongLettersThenLoseGame(self):
        ahorcado = Ahorcado("Universidad")
        riskedLetters = ["z","y","f","w","o","m"]
        for i in range(0,5,1):
            ahorcado.riskLetter(riskedLetters[i])
        self.assertEqual(ahorcado.riskLetter(riskedLetters[5]),"Game Over")

    def test_getRightWord(self):
        word = "Universidad"
        ahorcado = Ahorcado(word)
        rightWord = ahorcado.getRightWord()
        self.assertIsInstance(rightWord,str)
        self.assertTrue(rightWord.strip() != "")
        self.assertEqual(word, rightWord) """

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