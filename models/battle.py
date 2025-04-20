from models.startup import StartUp

class Battle:
    def __init__(self, startup1:StartUp, startup2:StartUp):
        self.startup1 = startup1
        self.startup2 = startup2
        self.battles = []
        
    def __str__(self):
        return f"\033[91m{self.startup1.name} vs {self.startup2.name}\033[0m"
        
    def show_list_battles():
        index = 0
        for battle in Battle.battles:
            print(Battle.battles[index])
            index += 1

    def manage_battle():
        pass