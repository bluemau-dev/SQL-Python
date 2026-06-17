import requests
import sqlite3

from config import TMDB_API_KEY # Reference API Key

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

def search_movie(title: str):
    url = "https://api.themoviedb.org/3/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": title
    }

    response = requests.get(url, params=params).json()

    movie = response["results"][0] # Results has its own List
    movie_data = get_details(movie.get("id"))

    title = movie_data.get("title")
    media_type = "movie"
    creator = [
        company['name']
        for company in movie_data.get("production_companies", [])
    ]
    release_year = movie_data.get("release_date")
    genre = [
        genres['name']
        for genres in movie_data.get("genres")
    ]

    runtime = movie_data.get("runtime")
    image_url = movie_data.get("poster_path")
    external_id = movie_data.get("id")


    print(f"Title: {title}")
    print(f"Media Type: {media_type}")
    print(f"Creator: {creator}")
    print(f"Release Year: {release_year}")
    print(f"Genres: {genre}")
    print(f"Length of Movie: {runtime}")
    print(f"Image URL: {image_url}")
    print(f"ID: {external_id}")


def get_details(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": TMDB_API_KEY,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()

def main():
    # Establish Database
    connection = sqlite3.connect("media.db")
    create_table(connection)

    search_movie("Cinderella")

if __name__ == '__main__':
    main()