from flask import Flask
from src.common.database import Database


app = Flask(__name__)

app.config.from_object('config')
app.secret_key = "123"


@app.before_first_request
def init_db():
    Database.initialize()


import src.route
import src.registered_components
