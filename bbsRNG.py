class bbsRNG:

    modulus = 0xE2089EA5
    
    def __init__(self, seed):
        self.currentValue = seed
        
    def nextInt(self):
        self.currentValue = (self.currentValue * self.currentValue) % self.modulus
        return self.currentValue
