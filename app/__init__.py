"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7qat269vf5qbal8lg-a.oregon-postgres.render.com",
        database="todo_ro0k",
        user="root",
        password="jNaLgP2IhveGJLalbaHR5gQjSgKz2hK2")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
