from flask import Blueprint, jsonify
from models import User, Product, Order, db

main_routes = Blueprint('main', __name__)

@main_routes.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'description': p.description, 'price': p.price} for p in products])

@main_routes.route('/register', methods=['POST'])
def register_user():
    # Registration logic will be implemented here
    return jsonify({'message': 'User registered successfully.'})

@main_routes.route('/login', methods=['POST'])
def login_user():
    # Login logic will be implemented here
    return jsonify({'message': 'User logged in successfully.'})
