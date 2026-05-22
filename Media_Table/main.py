import sqlite3

# Connect to Database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name) # Connect
    except Exception as e:
        print(f"Error: {e}")

def create_table(connection):
    
    # QUERY is an SQL Command
    QUERY = """ 
    CREATE TABLE IF NOT EXISTS media (
        media_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        media_type TEXT,
        release_year INT,
        description TEXT,
        creator TEXT
    )"""

    try:
        with connection: # Connect to SQL and execute command
            connection.execute(QUERY)
            print("Table was created!")
    except Exception as e:
        print(f"Error: {e} sorry!")

def main():

    # Database Name
    db_name = "media.db"
    # Connect to Database
    connection = sqlite3.connect(db_name)

    # Create a Cursor
    cur = connection.cursor()

    # Create Table
    create_table(connection)

if __name__ == '__main__':
    main()