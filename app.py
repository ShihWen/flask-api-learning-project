from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import os
import re

from security import authenticate
from security import identity
from resources.user import UserRegister

from resources.item import Item
from resources.item import ItemList
from resources.store import Store
from resources.store import StoreList

from db import db

# Reference: 
# https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres
uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLAKCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'apple'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')




if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
    