from flask import Flask, request, jsonify
from src.business_logic import BusinessLogic

app = Flask(__name__)
business_logic = BusinessLogic()


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(business_logic.get_all_users())