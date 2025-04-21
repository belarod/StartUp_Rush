from models.startup import StartUp

class Battle:
    def __init__(self, startup1:StartUp, startup2:StartUp):
        self.startup1 = startup1
        self.startup2 = startup2
        
    def __str__(self):
        return f"\033[91m{self.startup1.name} vs {self.startup2.name}\033[0m"
    
    def  get_tuple(self):
        return (self.startup1, self.startup2)
            
    @staticmethod
    def create_battle(startup1:StartUp, startup2:StartUp):
        return Battle(startup1, startup2)