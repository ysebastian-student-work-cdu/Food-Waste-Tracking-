from django.db import connection
from django.http import HttpResponse

def table_list(request):
    # Get the cursor from the database connection
    cursor = connection.cursor()

    # Execute the SQL query to fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all the table names from the cursor
    tables = [table[0] for table in cursor.fetchall()]

    # Construct a simple HTML response with the table names
    response = "<h2>Database Tables:</h2>"
    for table in tables:
        response += f"<p>{table}</p>"

    return HttpResponse(response)

