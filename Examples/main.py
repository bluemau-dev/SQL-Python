import sqlite3

# Connect to Database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name) # Connect
    except Exception as e:
        print(f"Error: {e}")
# Create a table in database
def create_table(connection):
    # QUERY is an SQL Command
    QUERY = """ 
    CREATE TABLE IF NOT EXISTS devices (
        device_id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_name TEXT,
        ip_address TEXT UNIQUE
    )
    """

    try:
        with connection: # Connect to SQL and execute command
            connection.execute(QUERY)
            print("Table was created!")
    except Exception as e:
        print(f"Error: {e} sorry!")
# Add / Insert a device to our Database
def insert_device(connection, device_name:str, ip_address:str):
    # Query to Add Data
    QUERY = """
    INSERT INTO devices (device_name, ip_address) VALUES (?,?) 
    """

    try:
        with connection:
            connection.execute(QUERY, (device_name, ip_address))
            print("Data was added!")
    except Exception as e:
        print(f"{e}")
# Select from device table
def select_device(connection):
    QUERY = "SELECT * FROM devices" # Select all rows
    
    try:
        with connection:
            cursor = connection.execute(QUERY)
            rows = cursor.fetchall()

            for row in rows:
                print(row)

    except Exception as e:
        print(e)
# Change data
def update_device(connection, device_name:str, device_id:int):
    QUERY = """
    UPDATE devices
    SET device_name = ?
    WHERE device_id = ?
    """

    try:
        with connection:
            connection.execute(QUERY, (device_name, device_id))
            print("Device updated!")
    
    except Exception as e:
        print(e)
# Delete Data
def delete_device(connection, device_id:int):
    QUERY = "DELETE FROM devices WHERE device_id = ?"

    try:
        with connection:
            connection.execute(QUERY, (device_id,))
            print(f"Device ID: {device_id} was deleted.")
    except Exception as e:
        print(e)


def main():
    connection = get_connection("network.db") # Establish Connection
    
    try:
        # If/Else Condition
        start = input("Enter option: (update, delete) ").lower()

        # Create table
        create_table(connection)

        # Insert Data
        device_name = "Laptop"
        ip_address = "192.9.0.5"
        insert_device(connection, device_name, ip_address)
        
        # Select Data
        select_device(connection)

        if start == "update":
            # Update Data
            new_name = "Switch"
            condition = int(input("Enter your device number: "))
            update_device(connection, new_name, condition)
        
        elif start == "delete":
            condition = int(input("Enter your device id: "))
            delete_device(connection, condition)

    finally:
        connection.close()


if __name__ == "__main__":
    main()