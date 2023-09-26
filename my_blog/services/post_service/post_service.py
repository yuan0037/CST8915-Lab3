from flask import Flask, jsonify
import requests

import os


app = Flask(__name__)

flask_app = os.environ.get('FLASK_APP')
print(f"FLASK_APP: {flask_app}")

@app.route('/')
def hello_world():
    return 'Hello, post service!'


@app.route('/post/<id>')
def post(id):
    posts = {
        '1': {'user_id': '1', 'post': 'Hello, world!'}, 
        '2': {'user_id': '2', 'post': 'My first blog post'}
    }
    post_info = posts.get(id, {})
    if post_info:
        response = requests.get(f'http://user_service:5000/user/{post_info["user_id"]}')
        if response.status_code == 200:
            post_info['user'] = response.json()
    return jsonify(post_info)

if __name__ == '__main__':
    app.run(port='5000')