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
        def list_startup_events(self):
                return self.events
        
        def create_event(index, title_of_events, points):
                event = StartUpEvents(title_of_events, points)
                StartUpEvents.events.append(event)
                return Option.add_option(index, event.title_of_event+f" ({event.points} pontos)") and event
        
        def evaluate_according_to_event(startup, event):
                if event.title_of_event in startup.events_done:
                        print(f"\033[91m{event.title_of_event} já foi feito!\033[0m")
                        Utils.sleep(2)
                        return
                else:
                        startup.score += event.points
                        startup.events_done.append(event.title_of_event)
                        print(f"\033[92m{event.title_of_event}, {event.points} pontos!\033[0m")
                        Utils.sleep(2)       