import random
from utils.utils import Utils
from models.startup import StartUp
from models.battle import Battle

class Tournament:
    def __init__(self):
        self.startups = [self.startup1, self.startup2, self.startup3, self.startup4, self.startup5, self.startup6, self.startup7, self.startup8]#TODO test 8
        #self.startups = [self.startup1, self.startup2, self.startup3, self.startup4, self.startup5, self.startup6, self.startup7]#TODO test impar
        #self.startups = [self.startup1, self.startup2, self.startup3, self.startup4] #TODO test 4
        #self.startups = [self.startup1, self.startup2, self.startup3] #TODO test -4 registradas
        self.battles = []
        self.winner = []
        
    startup1 = StartUp("Startup 1", "Slogan 1", 2020)
    startup2 = StartUp("Startup 2", "Slogan 2", 2021)  
    startup3 = StartUp("Startup 3", "Slogan 3", 2022)
    startup4 = StartUp("Startup 4", "Slogan 4", 2023)  
    startup5 = StartUp("Startup 5", "Slogan 5", 2024)
    startup6 = StartUp("Startup 6", "Slogan 6", 2025)
    startup7 = StartUp("Startup 7", "Slogan 7", 2026)
    startup8 = StartUp("Startup 8", "Slogan 8", 2027)
        
    def __len__(self):
        return len(self.startups)
       
    def list_startups(self):
        return self.startups
            
    def show_list_startups(self):
        count = 1
        for startup in self.startups:
            print(f"\033[31m{count}-> {startup.name}\033[0m")
            count += 1
        
    def register_startup(self,
                        startup:StartUp):
        if len(self.startups) < 8:
            self.startups.append(startup)
            print(f"Startup {startup.name} foi registrada!")
        else:
            print("O torneio já está cheio!")
            
    def remove_startup(self, 
                       index:int):
        startup = self.startups[index-1]
        if startup in self.startups:
            self.startups.remove(startup)
            print(f"Startup {startup.name} foi removida!")
        else:
            print("Startup não encontrada!")
            
    def is_registered_startups_even(self):
        if len(self.startups) % 2 == 0:
            return True
        else:
            return False
            
    def generate_battle_pairs(self): #TODO
        random.shuffle(self.startups)
        for startup_index in range(0, len(self.startups), 2):
            if startup_index + 1 < len(self.startups):
                battle = self.create_battle(self.startups[startup_index], self.startups[startup_index + 1])
                self.battles.append(battle)
        return self.battles
    
    def create_battle(self, startup1:StartUp, startup2:StartUp):#TODO neccessario?
        battle = Battle(startup1, startup2)
        return battle
                
            
    def isThereWinner(self):
        if len(self.startups) == 1:
            self.winner.append(self.startups[0])
            return True
        else:
            return False
        
    @staticmethod
    def show_tournament_title():
        Utils.clear_screen()
        print("\033[92m=========================\033[0m")
        print("\033[94m      STARTUP RUSH!\033[0m")
        print("\033[92m=========================\033[0m")