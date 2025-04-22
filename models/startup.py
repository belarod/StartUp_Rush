from utils.utils import Utils

from models.startup_events import StartUpEvents

class StartUp:
    def __init__(self,
                name:str,#criando
                slogan:str,#criando
                year_of_foundation:int,#criando
                score: int = 70,#criando
                quantity_of_occurrence_pitches: int = 0,#inserindo
                quantity_of_occurrence_bugs: int = 0,#inserindo
                quantity_of_occurrence_user_traction: int = 0,#inserindo
                quantity_of_occurrence_angry_investors: int = 0,#inserindo
                quantity_of_occurrence_pitches_with_fakenews: int = 0#inserindo
                ):
        self.name = name
        self.slogan = slogan
        self.year_of_foundation = year_of_foundation
        
        self.score = score
        self.quantity_of_occurrence_pitches = quantity_of_occurrence_pitches
        self.quantity_of_occurrence_bugs = quantity_of_occurrence_bugs
        self.quantity_of_occurrence_user_traction = quantity_of_occurrence_user_traction
        self.quantity_of_occurrence_angry_investors = quantity_of_occurrence_angry_investors
        self.quantity_of_occurrence_pitches_with_fakenews = quantity_of_occurrence_pitches_with_fakenews
        
        self.events_done = []
        
    @staticmethod
    def input_startup_name():
        name = input("Nome: ")
        return name
    
    @staticmethod
    def input_startup_slogan():
        slogan = input("Slogan: ")
        return slogan
    
    @staticmethod
    def input_startup_year_of_foundation():
        year_of_foundation = Utils.int_input("Ano de fundação (YYYY): ")
        if len(str(year_of_foundation)) != 4:
            return StartUp.input_startup_year_of_foundation()
        return year_of_foundation