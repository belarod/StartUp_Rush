class StartUp:
    def __init__(self,
                name:str,
                slogan:str,
                year_of_foundation:int,
                score: int = 70,
                quantity_of_occurrence_pitches: int = 0,
                quantity_of_occurrence_bugs: int = 0,
                quantity_of_occurrence_user_traction: int = 0,
                quantity_of_occurrence_angry_investors: int = 0,
                quantity_of_occurrence_pitches_with_fakenews: int = 0
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