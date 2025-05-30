import sqlite3

from models.startup import StartUp

class DB:  
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.__setup_tables()
        
    def __setup_tables(self):
        cur = self.connection.cursor()
        
        cur.execute('''
            CREATE TABLE IF NOT EXISTS startup (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                slogan TEXT,
                year_of_foundation INT,
                score INT
            )
            ''')
        
        cur.execute('''
            CREATE TABLE IF NOT EXISTS startup_event (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                startup TEXT,
                event INT
            )
            ''')
        
        cur.execute('''
            CREATE TABLE IF NOT EXISTS event (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title_of_event TEXT,
                points INT
            )
            ''')
        self.connection.commit()  
        cur.close()
        
    def create_startup(self, startup: StartUp):
        cur = self.connection.cursor()

        cur.execute('''INSERT INTO startup (name, slogan, year_of_foundation, score) VALUES (?, ?, ?, ?)''',
                    (startup.name, startup.slogan, startup.year_of_foundation, startup.score))
        self.connection.commit()
        cur.close()
        
    def create_event(self, event):
        cur = self.connection.cursor()

        cur.execute('''INSERT INTO event (title_of_event, points) VALUES (?, ?)''',
                    (event.title_of_event, event.points))
        self.connection.commit()
        cur.close()
        
    def insert_startup_event(self, startup_name, event_id): ##corrigir
        cur = self.connection.cursor()

        cur.execute('''INSERT INTO startup_event (startup, event) VALUES (?, ?)''',
                    (startup_name, event_id))
        self.connection.commit()
        cur.close()