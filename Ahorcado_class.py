class Ahorcado:
    
    rigthWord="Universidad"

    def __init__(self, rigthWord:str):
        self.rigthWord = rigthWord
        pass
    
    def riskWord(self,  riskedWord:str):
        #Win if is correct or lose if is not correct.
        if(riskedWord==self.rigthWord): 
            return True
        else:
            return False
        
    def riskLetter(self, riskedLetter:str):
        #Return True if the letter is correct. Another case, false.
        if ("U"==riskedLetter):
            return True
        else:
            return False

            