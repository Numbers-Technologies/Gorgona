# Database with settings for the Gorgona program
import sqlite3

class CreateDatabaseWithSettings:
    def __init__(self, database_name, database_path):
        self.database_name = database_name
        self.database_path = database_path
        self.create_database()

    def create_database(self):
        try:
            conn = sqlite3.connect(self.database_path)
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS settings (
                        name TEXT,
                        ip TEXT,
                        api_key TEXT,
                        telegram_session TEXT,
                        language TEXT,
                        dialogflow_id TEXT,
                        dialogflow_session TEXT,
                        dialogflow_token_path TEXT,
                        )""")
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)

CreateDatabaseWithSettings("settings.db", "Gorgona/settings.db")