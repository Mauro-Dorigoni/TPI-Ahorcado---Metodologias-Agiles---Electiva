class Ahorcado:
    
    rigthWord="Universidad"

    def __init__(self, rigthWord:str):
        self.rigthWord = rigthWord
        self.lives = 6
        pass
    
    def getRightWord(self):
        return self.rigthWord

    def riskWord(self,  riskedWord:str):
        #Win if is correct or lose if is not correct.
        if(riskedWord==self.rigthWord): 
            return True
        else:
            return False
        
    def riskLetter(self, riskedLetter:str):
        #Return True if the letter is correct. Another case, false.
        if (riskedLetter in self.rigthWord):    
            return True
        else:
            self.lives-=1
            if(self.lives == 0):
                return "Game Over"
            else:
                return False

            