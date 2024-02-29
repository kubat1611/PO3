from flask import Flask, request, jsonify
from src.api.business_logic import BusinessLogic

app = Flask(__name__)
business_logic = BusinessLogic()


def is_valid_user_data(user_data):
    valid_keys = ["first_name", "last_name", "birth_year", "group"]
    valid_groups = ["user", "premium", "admin"]

    if any(key in user_data for key in valid_keys):
        if "birth_year" in user_data and not isinstance(user_data["birth_year"], int):
            return False
        if "group" in user_data and user_data["group"] not in valid_groups:
            return False
        return True

    return False


@app.route('/')
def index():
    return 'Witaj użytkowniku!'


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
    if is_valid_user_data(user_data):
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        birth_year = user_data.get('birth_year')
        group = user_data.get('group')

        new_user = business_logic.create_user(first_name, last_name, birth_year, group)
        if new_user:
            return jsonify(new_user), 201
        else:
            return jsonify({'error': 'Failed to create user'}), 500
    else:
        return jsonify({'error': 'Invalid user data'}), 400


@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user_data = request.json
    updated_user = business_logic.update_user(user_id, user_data)

    if updated_user:
        return jsonify(updated_user), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted = business_logic.delete_user(user_id)
    if deleted:
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
