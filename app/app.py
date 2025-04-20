from utils.option import Option
from utils.utils import Utils
from models.tournament import Tournament
from models.startup import StartUp

class App:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            #self.db = db
            self._initialized = True
            self.tournament = Tournament()
    
    def start_app(self):
        #self.show_initializing_menu() 
        #self.show_manage_startups_menu() #teste
        self.show_register_startup_menu() #teste
        
    def exit_app(self):
        print("Saindo do aplicativo...")
        exit(0)
        
    def show_initializing_menu(self): #TODO métodos redirecionados
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Bem-vindo, Administrador!")
        Option.add_option(1, "Gerenciamento de StartUps")
        Option.add_option(2, "Sair")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if chosen_option == 1:
            self.show_manage_startups_menu()
        if chosen_option == 2:
            self.exit_app() 
                
    def show_manage_startups_menu(self): #TODO métodos redirecionados
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
            pass
        if chosen_option == 3:
            pass
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
        