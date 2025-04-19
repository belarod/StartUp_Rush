import os
#import time

class Utils:
    @staticmethod
    def clear_screen():
        '''Limpa terminal'''
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def sleep(seconds):
        '''Time'''
        if seconds < 0:
            raise ValueError("O tempo deve ser um valor não negativo.")
        if os.name == 'posix':
            os.system(f"sleep {seconds}")
        elif os.name == 'nt':
            os.system(f"timeout {seconds}")
        else:
            pass