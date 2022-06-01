#from django.shortcuts import render
import sqlite3

def version_prev():
    sqlite_connection = sqlite3.connect("/home/numbers/.config/Gorgona/settings.db")
    cursor = sqlite_connection.cursor()
    cursor.execute("select * from test;")
    record = cursor.fetchall()
    print(record[0][0])
    sqlite_connection.commit()
    cursor.close()

version_prev()

#def home(request):
    #return render(request, 'index.html')
