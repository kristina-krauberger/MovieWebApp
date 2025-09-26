from flask import Flask, jsonify
from data_manager import DataManager
from models.models import db, Movies
import os

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager(db) # Create an object of your DataManager class

# Testfunktion
@app.route('/')
def home():
    return "Welcome to MoviWeb App!"


@app.route('/users', methods=['GET'])
def list_users():
    users = data_manager.get_users()
    users_list = [{"id": user.id, "name": user.name} for user in users]  # List Comprehension, weil jsonify keine Objekte returnen kann
    return jsonify(users_list)


if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run()