# All of our imports
import sqlite3

# Setup / Initialize Database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise
# Create a Table in the Database
def create_table(connection):
    # SQL Syntax
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """

    try:
        with connection:
            connection.execute(query)
        print("Table was created.")
    except Exception as e:
        print(f"Error: {e}")
        raise
# Add User to Database
def insert_user(connection, name:str, age:int, email:str):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"

    try:
        with connection:
            connection.execute(query, (name, age, email))
        print(f"User: {name} was added to your database.")
    except Exception as e:
        print(e)
# Query all Users in Database
def fetch_users(connection, condition: str = None) -> list[tuple]: #(mauricio, 23, email)
    query = "SELECT * FROM users"
    if condition:
        query += f"WHERE {condition}"

    try:
        with connection:
            rows = connection.execute(query).fetchall()
        return rows
    except Exception as e:
        print(e)
# Delete a User from the Database
def delete_user(connection, user_id:int):
    query = "DELETE FROM users WHERE id = ?"
    try:
        with connection:
            connection.execute(query,(user_id,))
        print(f"USER ID: {user_id} was deleted!")
    except Exception as e:
        print(e)
# Updating a User from the Database
def update_user(connection, user_id:int, email:str):
    query = "UPDATE users SET email = ? WHERE id = ?"
    try:
        with conneection:
            connection.execute(query,(email, user_id))
        print(f"User ID {user_id}, has new email of {email}")
    except Exception as e:
        print(e)
# Ability to add Multiple Users
def insert_users(connection, users:list[tuple[str, int, str]]): 
    query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"
    try:
        with connection:
            connection.executemany(query, users)
        print(f"{len(users)} users were added to the database!")
    except Exception as e:
        print(e)

def main():
    connection = get_connection("pokemon.db")
    try:
        # Create my table
        create_table(connection)

        # SQL Commands
        start = input("Enter Option (Add, Delete, Update, Search, Add Many):").lower()
        
        if start == 'add':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            insert_user(connection, name, age, email)
        
        elif start == 'search':
            print("All Users: ")
            for user in fetch_users(connection):
                print(user)
        
        elif start == 'delete':
            user_id = int(input("Enter User ID: "))
            delete_user(connection, user_id)
        
        elif start == 'update':
            user_id = int(input("Enter User ID: "))
            new_email = input("Enter a new email: ")
            update_user(connection, user_id, new_email)

        elif start == 'add many':
            # Hardcoding Example of a List
            users = [
            ("Chandler", 20, "friends29@gmail.com"),
            ("Yoda", 29, "yoda@gmail.com"),
            ("Nebby", 10, "nebby@nebby.com")]
            insert_users(connection,users)

    finally:
        connection.close()

if __name__ == "__main__":
    main()
