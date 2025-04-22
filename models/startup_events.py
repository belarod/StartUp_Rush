from utils.option import Option
from utils.utils import Utils

class StartUpEvents:
        events = []
        
        def __init__(self,
                     title_of_event:str,
                     points:int = 0):
                self.title_of_event = title_of_event
                self.points = points
                
        @staticmethod
        def input_title_of_event():
                title_of_event = input("Título do evento: ")
                return title_of_event
        
        def input_points():
                points = Utils.int_input_accepts_negative("Pontos: ")#n aceita 0 nem num negativo
                return points

        def list_startup_events(self):
                return self.events
        
        @staticmethod
        def create_event(title_of_events, points):
                event = StartUpEvents(title_of_events, points)
                StartUpEvents.events.append(event)
                return event
        
        @staticmethod
        def evaluate_according_to_event(startup, event, index):
                if event.title_of_event in startup.events_done:
                        print(f"\033[91m{event.title_of_event} já foi feito!\033[0m")
                        Utils.press_to_continue("Pressione uma tecla para continuar...")
                        return
                else:
                        startup.score += event.points
                        startup.events_done.append(event.title_of_event)
                        
                        print(f"\033[92m{event.title_of_event}, {event.points} pontos!\033[0m") 
                        Utils.press_to_continue("Pressione uma tecla para continuar...")
                        
                        if index == 0:
                                startup.quantity_of_occurrence_convincing_pitches += 1
                        elif index == 1:
                                startup.quantity_of_occurrence_bugs += 1
                        elif index == 2:
                                startup.quantity_of_occurrence_user_traction += 1
                        elif index == 3:
                                startup.quantity_of_occurrence_angry_investors += 1
                        elif index == 4:
                                startup.quantity_of_occurrence_pitches_with_fakenews += 1