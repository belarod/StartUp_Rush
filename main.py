from app.app import App
from utils.utils import Utils
#from database.db import DB

if __name__ == '__main__':
    Utils.clear_screen()

    #my_db = DB('example.db')

    app = App()
    app.start_app()