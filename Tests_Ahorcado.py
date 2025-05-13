import unittest
from Ahorcado_class import Ahorcado


class TestAhorcado(unittest.TestCase):
  

    def test_RiskWrongWordThenLose(self):
        riskedWord = "palabra"
        ahorcado = Ahorcado("hola")
        self.assertFalse(ahorcado.riskWord(riskedWord))
        

    def test_RiskRightWordThenWin(self):
        riskedWord = "Universidad"
        ahorcado = Ahorcado(riskedWord)
        self.assertTrue(ahorcado.riskWord(riskedWord))
    
    def test_RiskWrongLetterThenLoseLife(self):
        riskedLetter = 'U'
        ahorcado = Ahorcado("Universidad")
        self.assertFalse(ahorcado.riskLetter(riskedLetter))
    

if __name__ == '__main__':
    unittest.main()