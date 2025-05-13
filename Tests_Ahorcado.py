import unittest
from Ahorcado_class import Ahorcado


class TestAhorcado(unittest.TestCase):
    def test_RiskWrongWordThenLose(self):
        riskedWord = "hola"
        self.assertFalse(Ahorcado.riskWord(riskedWord))
        
    def test_RiskWrongWordThenLose_v2(self):
        riskedWord = "palabra"
        self.assertFalse(Ahorcado.riskWord(riskedWord))

    def test_RiskRightWordThenWin(self):
        riskedWord = "Universidad"
        self.assertTrue(Ahorcado.riskWord(riskedWord))
    

if __name__ == '__main__':
    unittest.main()