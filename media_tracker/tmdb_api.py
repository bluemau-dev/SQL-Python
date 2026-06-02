import requests
import sqlite3

def create_table(connection): # Create Media Table
    query ="""
    CREATE TABLE IF NOT EXISTS media(
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    media_type TEXT NOT NULL,
    creator TEXT,
    release_year INTEGER,
    genre TEXT,
    runtime INTEGER,
    image_url TEXT,
    external_id INTEGER,
    UNIQUE (title, release_year)
    );
    """
    try:
        with connection:
            connection.execute(query)
    except Exception as e:
        print(e)

def insert_media(connection): # Insert Media (Movies/Shows)
    query = """
    INSERT OR IGNORE INTO media
    (title, media_type, creator, release_year, genre, runtime, image_url, external_id)
    VALUES (?,?,?,?,?,?,?,?);""" # 8 Values

    title = None
    media_type = None
    creator = None
    release_year = None
    genre = None
    runtime = None
    image_url = None
    external_id = None

    try:
        with connection:
            # VALIDATE FUNCTION

            # EXECUTE
            connection.execute(query, (title, media_type, creator, release_year, genre, runtime, image_url, external_id))
    
    except Exception as e:
        print(e)

def view_media(connection): # Execute and then Fetch
    query = "SELECT * FROM media;"

    try: # Executes Query
        cursor = connection.execute(query)

        # Fetches Rows in Table
        for row in cursor.fetchall():
            print(f"{row} ")
    except Exception as e:
        print(e)

def delete_media(connection): # Delete Media (Movies/Shows)
    query = """
    DELETE FROM media
    WHERE media_id = ?;
    """

    view_media(connection) # Show's Table
    media_id = int(input("\nEnter the Row you'd like to Delete: "))

    try:
        with connection:
            connection.execute(query, (media_id,))
    except Exception as e:
        print(e)

def main():
    # Establish Database
    connection = sqlite3.connect("media.db")
    create_table(connection)

if __name__ == '__main__':
    main()