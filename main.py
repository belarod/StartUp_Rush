from utils.utils import Utils
from database.database import DB
from app.app import App

if __name__ == '__main__':
    Utils.clear_screen()
    
    db = DB('database/startups.db')

    app = App(db)
    app.start_app()