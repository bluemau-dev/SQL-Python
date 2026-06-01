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
        creator TEXT,
        UNIQUE(title, release_year)
    )"""

    try:
        with connection: # Connect to SQL and execute command
            connection.execute(QUERY)
            print("Table was created!")
    except Exception as e:
        print(f"Error: {e} sorry!")

def insert_media(connection, data):
    
    # QUERY to INSERT DATA
    QUERY = """
     INSERT INTO media (title, media_type, release_year, description, creator)
     VALUES(?, ?, ?, ?, ?)"""

    try:
        with connection:
            connection.executemany(QUERY, data)
            connection.commit()
            print("Data was added.")
    except Exception as e:
        print(f"Error: {e} sorry!")

def select_all(connection):

    # QUERY to SELECT DATA
    QUERY = "SELECT * FROM media"

    try:
        cursor = connection.execute(QUERY)
        print("DATA:\n")

        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print(e)

def delete(connection):

    #QUERY
    QUERY = """
    DELETE FROM media
    WHERE media_id NOT IN (
        SELECT MIN(media_id)
        FROM media
        GROUP BY title, release_year
    );
    """

    try:
        with connection:
            connection.execute(QUERY)
            print("DELETED")
    except Exception as e:
        print(e)


def main():

    # Database Name
    db_name = "media.db"
    # Connect to Database
    connection = sqlite3.connect(db_name)

    # Create Table
    create_table(connection)
    
    #insert_media(connection, data)
    select_all(connection)
    #delete(connection)

if __name__ == '__main__':
    main()