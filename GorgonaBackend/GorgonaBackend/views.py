from django.shortcuts import render
from django.utils.translation import gettext as _
import sqlite3
import pwd
import os


def get_current_version() -> dict:
        sqlite_connection = sqlite3.connect(f"/home/{pwd.getpwuid(os.getuid()).pw_name}/.config/Gorgona/settings.db")
        cursor = sqlite_connection.cursor()
        cursor.execute("select * from test;")
        record = cursor.fetchall()
        cursor.close()
        print("===>", record)
        return {
            'report': _(record[0][0])
        }

def home(request):
    translations = get_current_version()
    return render(request, 'index.html',context={'translations': translations})
