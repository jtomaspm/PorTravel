from server import db

import os


def restart_db():
    os.remove("database.db")
    db.create_all()


restart_db()
