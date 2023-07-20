"""Main App"""
from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db

from resources.store import Store, StoreList, store_ns, stores_ns
from resources.item import Item, ItemList, item_ns, items_ns
from marshmallow import ValidationError

app = Flask(__name__)
blue_print = Blueprint('api', __name__, url_prefix='/api')
api = Api(blue_print, doc='/doc', title='Sample Flask-RestPlus Application')
app.register_blueprint(blue_print)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api.add_namespace(item_ns)
api.add_namespace(items_ns)
api.add_namespace(store_ns)
api.add_namespace(stores_ns)


@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


item_ns.add_resource(Item, '/<int:id>')
items_ns.add_resource(ItemList, '')
store_ns.add_resource(Store, '/<int:id>')
stores_ns.add_resource(StoreList, '')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5001, debug=True)
