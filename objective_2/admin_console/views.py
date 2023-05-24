from django.db import connection
from django.http import HttpResponse


def table_list(resquest):
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    response = "<h2>Database Tables:</h2>"
    for table in tables:
        response += f"<p>{table}</p>"
    return HttpResponse(response)