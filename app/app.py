from utils.option import Option
from utils.utils import Utils

from models.tournament import Tournament
from models.startup import StartUp
from models.startup_events import StartUpEvents
#from database.database import DB

class App:
    _instance = None
    _initialized = False
    
    evt1 = StartUpEvents.create_event("Pitch convincente", 6)
    evt2 = StartUpEvents.create_event("Produto com bugs", -4)
    evt3 = StartUpEvents.create_event("Boa tração de usuários", 3)
    evt4 = StartUpEvents.create_event("Investidores irritados", -6)
    evt5 = StartUpEvents.create_event("Pitch com fake news", -8)

    standard_events= [evt1, evt2, evt3, evt4, evt5]
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(App, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self._initialized = True
            #self.db = db
            self.tournament = Tournament()
            self.current_battle = None
    
    def start_app(self):
        self.show_initializing_menu() 
        #self.show_manage_startups_menu() #teste
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
        Option.add_option(4, "Criar evento surpresa!")
        Option.add_option(5, "Voltar ao menu inicial")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if chosen_option == 1:
            self.show_register_startup_menu() 
        if chosen_option == 2:
            self.show_remove_startup_menu()
        if chosen_option == 3:
            if Tournament.is_registered_startups_even(self.tournament) and len(self.tournament) >= 4 and len(self.tournament) <= 8:
                self.show_tournament_menu()
            else:
                print("Número de startups registradas deve ser par! Mínimo 4, máximo 8.")
                Utils.press_to_continue("Pressione uma tecla para continuar...")
                self.show_manage_startups_menu()
        if chosen_option == 4: 
            self.show_event_menu()
        if chosen_option == 5:
            self.show_initializing_menu()
            
    def show_register_startup_menu(self):
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Cadastro da StartUp")
        
        name = StartUp.input_startup_name()
        slogan = StartUp.input_startup_slogan()
        year_of_foundation = StartUp.input_startup_year_of_foundation()
        
        startup = StartUp(name, slogan, year_of_foundation)
        #DB.create_startup(self.db, startup)
        Tournament.register_startup(self.tournament, startup)
        Utils.press_to_continue("Pressione uma tecla para continuar...")
        self.show_manage_startups_menu()
        
    def show_remove_startup_menu(self):
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Remoção da StartUp")
        Tournament.show_startups_list_of_options(self.tournament)
        
        index = Option.choose_option("Escolha uma opção: ")
        Tournament.remove_startup(self.tournament, index)
        #funcao DB.remove
        Utils.press_to_continue("Pressione uma tecla para continuar...")
        self.show_manage_startups_menu()
        
    def show_event_menu(self):
        Tournament.show_tournament_title()
        Option.add_title_of_menu(f"Criação de evento surpresa")
        
        for event in StartUpEvents.events:
            print(f"\033[91m{event.title_of_event} -> {event.points} pontos\033[0m")
            
        Option.add_option(1, "Criar evento surpresa")
        Option.add_option(2, "Voltar ao gerenciamento de StartUps")
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if chosen_option == 1:
            title_of_event = StartUpEvents.input_title_of_event()
            points = StartUpEvents.input_points()
            event = StartUpEvents(title_of_event, points)
            StartUpEvents.create_event(title_of_event, points)
        if chosen_option == 2:
            self.show_manage_startups_menu()
        
        
        print(f"Evento '{event.title_of_event}' criado com sucesso!")
        Utils.press_to_continue("Pressione uma tecla para continuar...")
        self.show_manage_startups_menu()
        
    def show_tournament_menu(self):
        if Tournament.is_there_winner(self.tournament):
            self.show_tournament_results_menu()
    
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Torneio")
        
        print("Batalhas sorteadas:")
        battles = Tournament.generate_battle_pairs(self.tournament)
        count = 1
        for battle in battles:
            Option.add_option(count, str(battle))
            count += 1
            
        chosen_option = Option.choose_option("Escolha a batalha a ser gerenciada: ")
        self.current_battle = battles[chosen_option - 1]
        self.show_battle_management_menu()
            
    def show_battle_management_menu(self):
        Tournament.show_tournament_title()
        
        startup1 = self.current_battle.startup1
        startup2 = self.current_battle.startup2
        Option.add_title_of_menu(f"{startup1.name} vs {startup2.name}")
        Option.add_option(1, f"{startup1.name} - {startup1.score} pontos")
        Option.add_option(2, f"{startup2.name} - {startup2.score} pontos")
        Option.add_option(3, "Encerrar avaliação da batalha")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if chosen_option == 1:
            self.show_startup_evaluation_menu(startup1)
        if chosen_option == 2:
            self.show_startup_evaluation_menu(startup2)
        if chosen_option == 3:
            Tournament.calculate_battle_winner(self.tournament, self.current_battle)#TODO resultado da batalha
            self.current_battle = None
            Utils.press_to_continue("Pressione uma tecla para continuar...")
            self.show_tournament_menu()
            
            
        
    def show_startup_evaluation_menu(self, startup:StartUp):
        Tournament.show_tournament_title()
        Option.add_title_of_menu(f"Avaliação da StartUp {startup.name} -> Score:{startup.score}")
        print(f"Quantidade de ocorrência de pitches convincentes {startup.quantity_of_occurrence_convincing_pitches}")
        print(f"Quantidade de ocorrência de bugs {startup.quantity_of_occurrence_bugs}")
        print(f"Quantidade de ocorrência de tração de usuários {startup.quantity_of_occurrence_user_traction}")
        print(f"Quantidade de ocorrência de investidores irritados {startup.quantity_of_occurrence_angry_investors}")
        print(f"Quantidade de ocorrência de pitches com fake news {startup.quantity_of_occurrence_pitches_with_fakenews}")
        
        count = 1
        for event in StartUpEvents.events:
            Option.add_option(count, f"{event.title_of_event} -> {event.points} pontos")
            count += 1
        Option.add_option(len(StartUpEvents.events)+1, "Voltar ao gerenciamento da batalha")
        
        chosen_option = Option.choose_option("Escolha uma opção: ")
        
        if chosen_option == len(StartUpEvents.events)+1:
            self.show_battle_management_menu()
        else:
            StartUpEvents.evaluate_according_to_event(startup, StartUpEvents.events[chosen_option-1], chosen_option-1)
            self.show_startup_evaluation_menu(startup) 
            
    def show_tournament_results_menu(self):
        winner = Tournament.get_winner(self.tournament)
        Tournament.show_tournament_title()
        Option.add_title_of_menu(f"-> {winner.slogan} // {winner.name} é vencedor!")
        
        Option.add_option(1, "Mostrar relatório do torneio")
        Option.add_option(2, "Voltar ao menu inicial")
        Option.add_option(3, "Sair")
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if chosen_option == 1:
            self.show_tournament_report_menu()
            chosen_option = Option.choose_option("RELATORIO")
        if chosen_option == 2:
            Tournament.reset_tournament(self.tournament)
            self.show_initializing_menu()
        if chosen_option == 3:
            self.exit_app()
            
    def show_tournament_report_menu(self):
        Tournament.show_tournament_title()
        Option.add_title_of_menu("Relatório do torneio")
       
        for startup in self.tournament.startups:
            print(f"\033[91m{startup.name} -> {startup.score} pontos\033[0m")
            print(f"Quantidade de ocorrência de pitches convincentes {startup.quantity_of_occurrence_convincing_pitches}")
            print(f"Quantidade de ocorrência de bugs {startup.quantity_of_occurrence_bugs}")
            print(f"Quantidade de ocorrência de tração de usuários {startup.quantity_of_occurrence_user_traction}")
            print(f"Quantidade de ocorrência de investidores irritados {startup.quantity_of_occurrence_angry_investors}")
            print(f"Quantidade de ocorrência de pitches com fake news {startup.quantity_of_occurrence_pitches_with_fakenews}")
            
        Option.add_option(1, "Voltar ao menu inicial")
        Option.add_option(2, "Sair")
        chosen_option = Option.choose_option("Escolha uma opção: ")
        if chosen_option == 1:
            self.show_initializing_menu()
        if chosen_option == 2:
            self.exit_app()