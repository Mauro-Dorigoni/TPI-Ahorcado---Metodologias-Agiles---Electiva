import random
class Ahorcado:   

    rightWord = ""

    def __init__(self):
        self.rightWord = self.__getWord()
        self.lives = 6
        pass
    
    def getRightWord(self):
        return self.rightWord

    def riskWord(self,  riskedWord:str):
        #Win if is correct or lose if is not correct.
        if(riskedWord==self.rightWord): 
            return True
        else:
            return False
        
    def riskLetter(self, riskedLetter:str):
        #Return True if the letter is correct. Another case, false.
        if (riskedLetter in self.rightWord):    
            return True
        else:
            self.lives-=1
            if(self.lives == 0):
                return "Game Over"
            else:
                return False

    def __getWord(self):
        with open('palabras.txt', 'r', encoding='utf-8') as f:
            palabras = [line.strip() for line in f if line.strip()]
            return random.choice(palabras).lower()

            