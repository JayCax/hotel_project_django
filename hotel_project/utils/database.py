from django.db import connection


def custom_sql_query():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM myapp_client WHERE ...")
        row = cursor.fetchone()
    return row
