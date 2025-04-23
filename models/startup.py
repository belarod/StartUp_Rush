from utils.utils import Utils
from tabulate import tabulate

from models.startup_events import StartUpEvents

class StartUp:
    def __init__(self,
                name:str,
                slogan:str,
                year_of_foundation:int,
                score: int = 70,
                quantity_of_occurrence_convincing_pitches: int = 0,
                quantity_of_occurrence_bugs: int = 0,
                quantity_of_occurrence_user_traction: int = 0,
                quantity_of_occurrence_angry_investors: int = 0,
                quantity_of_occurrence_pitches_with_fakenews: int = 0
                ):
        self.name = name
        self.slogan = slogan
        self.year_of_foundation = year_of_foundation
        
        self.score = score
        self.quantity_of_occurrence_convincing_pitches = quantity_of_occurrence_convincing_pitches
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
    
    def table(startups):
        startups_ordenadas_desc = sorted(startups, key=lambda s: s.score, reverse=True)
        
        table_data = []
        for s in startups_ordenadas_desc:
            table_data.append([
                s.name,
                s.slogan,
                s.year_of_foundation,
                s.score,
                s.quantity_of_occurrence_convincing_pitches,
                s.quantity_of_occurrence_bugs,
                s.quantity_of_occurrence_user_traction,
                s.quantity_of_occurrence_angry_investors,
                s.quantity_of_occurrence_pitches_with_fakenews
            ])
            
        headers = [
            "\033[91mNome\033[0m", 
            "\033[91mSlogan\033[0m", 
            "\033[91mAno\033[0m", 
            "\033[91mScore\033[0m", 
            "\033[91mPitches Conv.\033[0m", 
            "\033[91mBugs\033[0m", 
            "\033[91mTração de Users\033[0m", 
            "\033[91mInv. Irritados\033[0m", 
            "\033[91mFakenews\033[0m"
        ]
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
