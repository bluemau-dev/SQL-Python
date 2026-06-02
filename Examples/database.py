import sqlite3

# SQLlite Connection
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(e)

# Create Table
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS media(
    media_id INT PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    media_type TEXT,
    release_year INT,
    creator TEXT,
    description TEXT,
    UNIQUE(title, release_year)
    )"""

    try:
        with connection: # Execute QUERY to create table
            connection.execute(query)
    except Exception as e:
        print(e)

# Insert
def insert(connection, data):
    query = """
    INSERT OR IGNORE INTO media (title, media_type, release_year, creator, description)
    VALUES (?, ?, ?, ?, ?)"""
    
    try:
        with connection:
            connection.executemany(query, data)
            connection.commit()
            print("DATA INSERTED.")
    except Exception as e:
        print(e)


# Select
def select_all(connection):
    query = "SELECT * FROM media"

    try:
        cursor = connection.execute(query)

        for row in cursor.fetchall():
            print(row)
    except Exception as e:
        print(e)

# Delete
# Update


def main():
    # Establish Connection
    connection = get_connection("media.db")
    create_table(connection)
    
    

if __name__ == "__main__":
    main()