import os
#import time

class Utils:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def sleep(seconds):
        if seconds < 0:
            raise ValueError("O tempo deve ser um valor não negativo.")
        if os.name == 'posix':
            os.system(f"sleep {seconds}")
        elif os.name == 'nt':
            os.system(f"timeout {seconds}")
        else:
            pass
        
    @staticmethod
    def press_to_continue(msg):
        input(msg)
        
    @staticmethod    
    def int_input(msg):
        valid_option = False
        result = None
        
        while not valid_option:
            try:
                value = input(msg)
                result = int(value)
                valid_option = True
                
                if result < 0:
                    valid_option = False
                else:
                    valid_option = True
            except:
                continue
        return result