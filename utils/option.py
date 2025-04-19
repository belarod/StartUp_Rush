class Option:
    list_options = []
    
    def __init__(self,
                    option,
                    msg):
        self.option = option
        self.msg = msg
        
    @staticmethod
    def choose_option(msg):
        while True:
            try:
                option = int(input(msg))
                if option > 0:
                    return option
                else:
                    print('Digite um número positivo.')
            except:
                print('Digite o número correspondente do menu numérico.')
    
    @staticmethod
    def add_option(index, msg):
        option = Option(index, msg)
        option.list_options.append(option)
        
        print(f'{index}. {msg}')
    
    @staticmethod
    def analyze_option(option):
        if option in range(1, len(Option.list_options) + 1):
            return option
        else:
            print('Opção inválida.')
            Option.choose_option('Escolha uma opção: ')