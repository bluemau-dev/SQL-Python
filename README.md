# SQL-Python

# Plan:
1. Connect to Database.
2. Create a Table.
3. Create ability to INSERT, SELECT, UPDATE, DELETE data.

# Notes
The following segment of code will print the URL. This will help when some URL's require extra parameters to validate them.     print(response.url)

Had NULL properties in some fields inside the books.db To remove them...
        DELETE FROM books
        WHERE "x" IS NULL;

/a/olid : A means author image, not the book cover.


# Database Design
* Avoid storing duplicate informartion or unnecessary data
* Design the schema before writing insertion logic
* Choose appropriate constraints

# Data Validation
* Validate data before inserting it into the database
* Never assume API data is complete or correct
* Prevent cleaning / sanitizing data by handling it correctly

# API Design
* API endpoints may return different data structures
* Read JSON response before designing database

# API Key
--------
Identifies the application making the request.

# Access Token
------------
Carries permissions and determines what actions the requester is allowed to perform.

# Authentication
--------------
Who are you?

# Authorization
-------------
What are you allowed to do?

# TMDB_API.py
While creating this script, it has been easier to understand what is required from creating a database and getting information from an api. I've split the tasks into creating the database first to know exactly what I will need to gather from the API.

My next approach will be to throughly read the documentation for the API to understand what endpoints contain what data to get for my database. 

        # Issues
        1. Ensure when I create a table in SQL to ensure to add "IF NOT EXISTS" to make sure an
        instance of that table doesn't already exists.

        2. In SQL when using parameterized SQL queries... the vales are typically passed as a sequence (usually a tuple).

        Example:
        A -> Parameter is an integer which is NOT what SQL expects.
        B -> Parameter is a tuple which is what SQL expects since it is looking for a sequences of VALUES.

        a. connection.execute(query, media_id)
        b. connection.execute(query, (media_id,))

# config.py
---------
Stores application configuration and environment variables.

Examples:
- API Keys
- Database names
- URLs
- Settings

# Environment Variables

Purpose:
Store secrets and configuration outside of source code.

Examples:
- API Keys
- Database URLs
- Passwords
- Secret Keys

Files:
.env -> stores values
config.py -> loads values

Benefits:
- Prevents hardcoding secrets
- Easier configuration management
- Safer for GitHub projects


# tmdb_api.py

The following piece of code creates a new list that will get the key value pairs of 'name' from each dictionary that was extracted from the list of production companies from the TMDB API. So it will print out each production company in its own index inside of a list. 
creator = [
        company['name']
        for company in movie_data.get("production_companies", [])
    ]

# Shrek
creator = ["Pacific Data Images", "DreamWorks Animation", "DreamWorks Pictures"]