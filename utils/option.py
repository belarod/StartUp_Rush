class Option:
    list_options = []
    
    def __init__(self,
                    option,
                    msg):
        self.option = option
        self.msg = msg
        
    def choose_option(msg):
        option = input(msg)
        if option.strip() == "":
            print('Entrada vazia. Por favor, digite um número correspondente do menu numérico.')
            return Option.choose_option(msg)
        option = int(option)
        if option > 0 and option in range(1, len(Option.list_options) + 1):
            Option.list_options.clear()
            return option
        else:
            print('Digite um número correspondente do menu numérico.')
            return Option.choose_option(msg)
    
    @staticmethod
    def add_option(index, msg):
        option = Option(index, msg)
        Option.list_options.append(option)
        
        print(f'\033[1;32m{index}.\033[0m \033[94m{msg}\033[0m')
        
    @staticmethod
    def add_title_of_menu(title):
        print(f"\033[93m{title}\033[0m")
        
Option.add_title_of_menu("oi")