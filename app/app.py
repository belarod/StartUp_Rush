from utils.option import Option
from utils.utils import Utils
from models.tournament import Tournament
from models.startup import StartUp
from models.battle import Battle

class App:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._initialized = True
            self.tournament = Tournament()
            self.current_battle = None
    
    def start_app(self):
        #self.show_initializing_menu() 
        self.show_manage_startups_menu() #teste
        #self.show_register_startup_menu() #teste
        
    def exit_app(self):
        print("Saindo do aplicativo...")
        Utils.sleep(2)
        Utils.clear_screen()
        exit(0)
        
    def show_initializing_menu(self):
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Bem-vindo, Administrador!")
        Option.add_option(1, "Gerenciamento de StartUps")
        Option.add_option(2, "Sair")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if chosen_option == 1:
            self.show_manage_startups_menu()
        if chosen_option == 2:
            self.exit_app() 
                
    def show_manage_startups_menu(self):
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Gerenciamento de StartUps")
        Tournament.show_list_startups(self.tournament)
        
        Option.add_option(1, "Cadastrar StartUp")
        Option.add_option(2, "Remover StartUp") 
        Option.add_option(3, "Iniciar Torneio")
        Option.add_option(4, "Voltar ao menu inicial")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if chosen_option == 1:
            self.show_register_startup_menu() 
        if chosen_option == 2:
            self.show_remove_startup_menu()
        if chosen_option == 3:
            self.show_tournament_menu()
        if chosen_option == 4:
            self.show_initializing_menu()
            
    def show_register_startup_menu(self):
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Cadastro da StartUp")
        
        name = StartUp.input_startup_name()
        slogan = StartUp.input_startup_slogan()
        year_of_foundation = StartUp.input_startup_year_of_foundation()
        
        startup = StartUp(name, slogan, year_of_foundation)
        Tournament.register_startup(self.tournament, startup)
        Utils.sleep(2)
        self.show_manage_startups_menu()
        
    def show_remove_startup_menu(self):
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Remoção da StartUp")
        Tournament.show_list_startups(self.tournament)
        
        index = Option.choose_option("Escolha uma opção: ")
        Tournament.remove_startup(self.tournament, index)
        Utils.sleep(2)
        self.show_manage_startups_menu()
        
    def show_tournament_menu(self):
        if Tournament.is_registered_startups_even(self.tournament) and len(self.tournament) >= 4 and len(self.tournament) <= 8:
            Tournament.show_tournament_title()
            Option.add_title_of_menu("Torneio")
            
            battles = Tournament.generate_battle_pairs(self.tournament)
            count = 1
            for battle in battles:
                Option.add_option(count, str(battle))
                count += 1
                
            chosen_option = Option.choose_option("Escolha a batalha a ser gerenciada: ")
            self.current_battle = battles[chosen_option - 1]
            self.show_battle_management_menu()
        else:
            print("Número de startups registradas deve ser par! Mínimo 4, máximo 8.")
            Utils.sleep(2)
            self.show_manage_startups_menu()
            
    def show_battle_management_menu(self):
        Tournament.show_tournament_title()
        
        startup1 = self.current_battle.startup1
        startup2 = self.current_battle.startup2
        Option.add_title_of_menu(f"{startup1.name} vs {startup2.name}")
        Option.add_option(1, f"{startup1.name}")
        Option.add_option(2, f"{startup2.name}")
        Option.add_option(3, "Encerrar avaliação da batalha")
        chosen_option = Option.choose_option("Escolha uma StartUp a ser avaliada: ")
        if chosen_option == 1:
            self.show_startup_evaluation_menu(startup1)
        if chosen_option == 2:
            self.show_startup_evaluation_menu(startup2)
        if chosen_option == 3:
            pass #TODO
        
    def show_startup_evaluation_menu(self, startup:StartUp):
        Tournament.show_tournament_title()
        Option.add_title_of_menu(f"Avaliação da StartUp {startup.name}")
        
        Option.add_option(1, "Pitch convinvente: +6 pontos")
        Option.add_option(2, "Produto com bugs: -4 pontos")
        Option.add_option(3, "Boa tração de usuários: +3 pontos")
        Option.add_option(4, "Investidor irritado: -6 pontos")
        Option.add_option(5, "Fake news no pitch: -8 pontos")
        Option.add_option(6, "Voltar ao gerenciamento da batalha")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
    
        if chosen_option == 1:
            print(f"\033[1;32m{startup.name} ganhou 6 pontos!\033[0m")#TODO
            Utils.sleep(2)
            self.show_startup_evaluation_menu(startup)
        if chosen_option == 2:
            print(f"\033[1;31m{startup.name} perdeu 4 pontos!\033[0m")#TODO
            Utils.sleep(2)
            self.show_startup_evaluation_menu(startup)
        if chosen_option == 3:
            print(f"\033[1;32m{startup.name} ganhou 3 pontos!\033[0m")#TODO
            Utils.sleep(2)
            self.show_startup_evaluation_menu(startup)
        if chosen_option == 4:
            print(f"\033[1;31m{startup.name} perdeu 6 pontos!\033[0m")#TODO
            Utils.sleep(2)
            self.show_startup_evaluation_menu(startup)
        if chosen_option == 5:
            print(f"\033[1;31m{startup.name} perdeu 8 pontos!\033[0m")#TODO
            Utils.sleep(2)
            self.show_startup_evaluation_menu(startup)
        if chosen_option == 6:
            self.show_battle_management_menu()