from flask import Flask, request, jsonify
from src.business_logic import BusinessLogic

app = Flask(__name__)
business_logic = BusinessLogic()


@app.route('/')
def index():
    return 'Witaj'


@app.route('/users', methods=['GET'])
def get_users():
    users = business_logic.get_all_users()
    return jsonify(users), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = business_logic.get_user(user_id)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    if business_logic.is_valid_user_data(user_data):
        new_user = business_logic.create_user(user_data)
        return jsonify(new_user), 201
    else:
        return jsonify({'error': 'Invalid user data'}), 400


@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user_data = request.json
    if business_logic.is_valid_user_data(user_data):
        updated_user = business_logic.update_user(user_id, user_data)
        if updated_user:
            return jsonify(updated_user), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Invalid user data'}), 400


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = business_logic.delete_user(user_id)
    if deleted:
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
