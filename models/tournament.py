import random
from utils.utils import Utils
from models.startup import StartUp
from models.battle import Battle
from utils.option import Option
from models.startup_events import StartUpEvents

class Tournament:
    event_shark_fight = StartUpEvents("Shark Fight", 2)
    
    def __init__(self):
        #self.startups = [self.startup1, self.startup2, self.startup3, self.startup4, self.startup5, self.startup6, self.startup7, self.startup8]#TODO test 8
        #self.startups = [self.startup1, self.startup2, self.startup3, self.startup4, self.startup5, self.startup6, self.startup7]#TODO test impar
        self.startups = [self.startup1, self.startup2, self.startup3, self.startup4] #TODO test 4
        #self.startups = [self.startup1, self.startup2, self.startup3] #TODO test -4 registradas
        self.battles = []
        self.winner = [] #TODO
        
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
            
    def show_startups_list_of_options(self):
        count = 1
        for startup in self.startups:
            Option.add_option(count, startup.name)
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
                battle = Battle.create_battle(self.startups[startup_index], self.startups[startup_index + 1])
                self.battles.append(battle)
        return self.battles
    
    def calculate_battle_winner(self, battle:Battle):
        startup1 = battle.startup1
        startup2 = battle.startup2
        
        if startup1.score == startup2.score:
            self.do_shark_fight(battle)
            self.calculate_battle_winner(battle)
            
        elif startup1.score > startup2.score: 
            self.remove_startup_loser(startup2)
            self.add_startup_winner(startup1)
            
            print(f"\033[92m{startup1.name} venceu!\033[0m")   
        elif startup1.score < startup2.score:   
            self.remove_startup_loser(startup1)
            self.add_startup_winner(startup2)
            
            print(f"\033[92m{startup2.name} venceu!\033[0m")
        
        for battle in self.battles:
            if battle.get_tuple() == battle.get_tuple():
                self.battles.remove(battle)
        
    def show_existing_battles(self):#TODO
        count = 1
        for battle in self.battles:
            Option.add_option(count, str(battle))
            count += 1
        return self.battles
        
    def do_shark_fight(self, battle:Battle):
        winner = random.randint(0,1)
        battle.get_tuple()[winner].score += 2
            
    def is_there_winner(self):
        if len(self.startups) == 1:
            self.winner.append(self.startups[0])
            return True
        else:
            return False
        
    def remove_startup_loser(self, startup:StartUp):
        self.startups.remove(startup)
        
    def add_startup_winner(self, startup:StartUp):
        self.startups.append(startup)
        
    @staticmethod
    def show_tournament_title():
        Utils.clear_screen()
        print("\033[92m=========================\033[0m")
        print("\033[94m      STARTUP RUSH!\033[0m")
        print("\033[92m=========================\033[0m")