import random
import string

class Ahorcado:   

    rightWord = ""
    possible_letters = set(string.ascii_lowercase) #All simbols in the alphabet [65,90]

    def __init__(self):
        self.rightWord = self.__getWord()
        self.lives = 6
        self.wordState = ['_' for _ in self.rightWord]
        self.riskedLetters = set()
        pass
    
    def getWordState(self):
        return ''.join(self.wordState)

    def getRightWord(self):
        return self.rightWord

    def riskWord(self,  riskedWord:str):
        #Win if is correct or lose if is not correct.
        if(riskedWord==self.rightWord): 
            return True
        else:
            return False
        
    def riskLetter(self, riskedLetter:str):
        #Return True if the letter is correct. If not sustrct one life, and return False. If lives == 0, return "Game over". Add letter to riskedLetters
        riskedLetter = riskedLetter.lower()

        #Verifies that the letter hasn't been risked before
        if riskedLetter in self.riskedLetters:
            return False
        
        self.riskedLetters.add(riskedLetter)

        if (riskedLetter in self.rightWord):    
            return True
        else:
            self.lives-=1
            if(self.lives == 0):
                return "Game Over"
            else:
                return False 

    def getRiskedLetters(self):
        return self.riskedLetters

    def __getWord(self):
        with open('palabras.txt', 'r', encoding='utf-8') as f:
            palabras = [line.strip() for line in f if line.strip()]
            return random.choice(palabras).lower()

            