from utils.option import Option
from models.tournament import Tournament

class App:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance
    
    def start_app(self):
        #self.show_initializing_menu()
        self.show_register_startup_menu()
        
    def exit_app(self):
        print("Saindo do aplicativo...")
        exit(0)
        
    def show_initializing_menu(self): #TODO métodos redirecionados
        print("StartUp Rush! // administração")
        Option.add_option(1, "Cadastro de StartUps")
        Option.add_option(2, "Sair")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if Option.analyze_option(chosen_option):
            if chosen_option == 1:
                self.show_register_startup_menu() 
            elif chosen_option == 2:
                self.exit_app() 
                
    def show_register_startup_menu(self): #TODO métodos redirecionados
        print("Cadastro de StartUps")
        Option.add_option(1, "Cadastrar StartUp")
        Option.add_option(2, "Remover StartUp")
        Option.add_option(3, "Iniciar Torneio")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if Option.analyze_option(chosen_option):
            if chosen_option == 1:
                self.register_startup() 
            elif chosen_option == 2:
                self.list_startups()
            elif chosen_option == 3:
                self.show_initializing_menu()