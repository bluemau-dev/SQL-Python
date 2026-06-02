import requests
import sqlite3

def search_book(connection):
    
    # Prompt Input
    book_title = input("Enter the title of the book: ")

    # API Endpoint
    url = 'https://openlibrary.org/search.json'

    try:
        response = requests.get(url, params={"title": book_title})
        response.raise_for_status()

        data = response.json()
        book = data['docs'][0]

        print(f"Publish Year: {book['first_publish_year']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author_name']}")
        print(f"Key: {book['author_key']}")

        # Prompt User to Save
        save_to_database(connection, book)
        
    except IndexError:
        print(f"The following book '{book_title}' could not be found or was spelled incorrectly.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

def get_book_to_database():
    pass 

def search_author(connection):

    # Prompt Input
    author = input("Enter the authors first and last name: ")

    # API Endpoint
    url = 'https://openlibrary.org/search/authors.json'

    try:
        response = requests.get(url, params={"q": author})
        response.raise_for_status()

        data = response.json()
        author_data = data['docs'][0]
        key = author_data['key']

        # Print Author Data
        print(f"Author: {author_data['name']}")
        #print(f"Top Subjects: {author_data['top_subjects']}")
        print(f"Key: {author_data['key']}")

        # Author's Books
        get_author_works(connection, author)
        

    except IndexError:
        print(f"No author found for '{author}', try a different name.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

def get_author_works(connection, author):
    # API Endpoint
    #url = f'https://openlibrary.org/authors/{key}/works.json'
    url = f'https://openlibrary.org/search.json'

    try:
        #response = requests.get(url)
        response = requests.get(url, params={"author": author})
        response.raise_for_status()

        data = response.json()
        books = data['docs']

        # Index and Data of the List
        for index, book in enumerate(books):
            print(f"{index}: {book['title']}")

            if index == 9: # Stop at six Books (0-5)
                break
        
        # Prompt User to View Book Details
        choice = int(input("\nEnter the number of the book to see details: "))
        if 0 <= choice < len(books):
            get_book_details(connection, books[choice])
        else:
            print("Invalid choice.")

    except IndexError:
        print(f"No author found.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

def get_book_details(connection, book): # book -> Of Mice and Men
    # book['key'] -> "/works/OL45804W"
    url = f"https://openlibrary.org{book['key']}.json"
    
    try:   
        response = requests.get(url)
        response.raise_for_status()

        book = response.json()

        print(f"Title: {book.get('title')}")
        print(f"Description: {book.get('description')}")
        print(f"Subject: {book.get('subjects')}")

        save = input("Save this book to database? y/n ")
        if save.lower() == "y":
            insert_book(connection, book)
            print("Book saved.")
    
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS books(
    media_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    publish_year INTEGER,
    work_key TEXT,
    UNIQUE(title, publish_year)
    )"""

    try:
        with connection: # Execute QUERY to create table
            connection.execute(query)
    except Exception as e:
        print(e)

def insert_book(connection, book):
    query = """
    INSERT OR IGNORE INTO books (title, author, publish_year, work_key)
    VALUES (?,?,?,?)
    """

    # Data -> Values
    title = book.get("title")
    author = ", ".join(book.get("author_name", []))
    publish_year = book.get("first_publish_year")
    work_key = book.get("key")

    # Execute Query
    with connection:
        connection.execute(query, (title,author,publish_year,work_key))

def save_to_database(connection, book):

    save = input("Save this book to database? y/n ")
    if save.lower() == "y":
        insert_book(connection, book)
        print("Book saved.")

def main():
    
    connection = sqlite3.connect("books.db")
    create_table(connection)

    options = {
        1: search_book,
        2: search_author,
    }

    x = int(input("Enter one of the following:\n1.Book Name.\n2.Author's Name.\n"))
    action = options.get(x)

    if action:
        action(connection)
    else:
        print("Invalid option.")
    
    
if __name__ == '__main__':
    main()
