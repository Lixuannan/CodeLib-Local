import sys

import ui

import sqlite3

settings = {}
default_site = []


def show_settings():
    for i in settings:
        print(f"{i}: {settings[i]}")


if __name__ == '__main__':
    main = ui.UI()
    db = sqlite3.connect("data.db")
    cursor = db.execute("SELECT * FROM settings")
    for i in cursor:
        value = None
        for j in i:
            if j is not None:
                value = j
        settings[i[0]] = value
    show_settings()

    cursor = db.execute("SELECT * FROM default_sync")
    for i in cursor:
        if i[1]:
            default_site.append(i[0])
    print(f"Default site: {default_site}")

    sys.exit(main.app.exec())

