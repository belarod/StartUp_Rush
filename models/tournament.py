from utils.utils import Utils
from models.startup import StartUp

class Tournament:
    def __init__(self):
        self.startups = []
        self.winner = []
        
    def __len__(self):
        return len(self.startups)
    
    def list_startups(self):
        if len(self.startups) == 0:
            print("Nenhuma startup registrada.")
        else:
            startup_names = []
            for startup in self.startups:
                startup_names.append(startup.name)
            print(f"Startups registradas:{startup_names}")
        
    def register_startup(self,
                        startup:StartUp):
        if len(self.startups) < 8:
            self.startups.append(startup)
            print("Startup registrada com sucesso!")
        else:
            print("O torneio já está cheio!")
            
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
            
tournament = Tournament()
tournament.register_startup(StartUp("Startup 1", "Inovação", 2023))
tournament.register_startup(StartUp("Startup 2", "Inovação", 2022))
tournament.register_startup(StartUp("Startup 3", "Inovação", 2022))
tournament.register_startup(StartUp("Startup 4", "Inovação", 2022))
tournament.register_startup(StartUp("Startup 5", "Inovação", 2022))
tournament.register_startup(StartUp("Startup 6", "Inovação", 2022))
tournament.register_startup(StartUp("Startup 7", "Inovação", 2022))
tournament.register_startup(StartUp("Startup 8", "Inovação", 2022))
tournament.register_startup(StartUp("Startup 8", "Inovação", 2022))
tournament.list_startups()