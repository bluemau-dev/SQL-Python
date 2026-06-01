import requests

def search_book():
    
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
        
    except IndexError:
        print(f"The following book '{book_title}' could not be found or was spelled incorrectly.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

def get_book_to_database():
    pass 

def search_author():

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
        print(f"Top Subjects: {author_data['top_subjects']}")
        print(f"Key: {author_data['key']}")

        # Author's Books
        get_author_works(key)
        

    except IndexError:
        print(f"No author found for '{author}', try a different name.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

def get_author_works(key):
    # API Endpoint
    url = f'https://openlibrary.org/authors/{key}/works.json'

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        books = data['entries']

        # Index and Data of the List
        for index, book in enumerate(books):
            print(f"{index}: {book['title']}")

            if index == 9: # Stop at six Books (0-5)
                break
        
        # Prompt User to View Book Details
        choice = int(input("\nEnter the number of the book to see details: "))
        if 0 <= choice <= len(books):
            get_book_details(books[choice])
        else:
            print("Invalid choice.")

    except IndexError:
        print(f"No author found.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

def get_book_details(book): # book -> Of Mice and Men
    # book['key'] -> "/works/OL45804W"
    url = f"https://openlibrary.org{book['key']}.json"
    
    try:   
        response = requests.get(url).json()
        response.raise_for_status()

        data = response.json()

        print(f"Title: {data.get('title')}")
        print(f"Description: {data.get('description')}")
        print(f"Subject: {data.get('subjects')}")
    
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        

def main():
    
    options = {
        1: search_book,
        2: search_author,
    }

    x = int(input("Enter one of the following:\n1.Book Name.\n2.Author's Name.\n"))
    action = options.get(x)

    if action:
        action()
    else:
        print("Invalid option.")
    
    
if __name__ == '__main__':
    main()
