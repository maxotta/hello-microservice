#
# Hello microservice example.
#
# pip3 install Flask

from flask import Flask
import socket

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    hostname = socket.gethostname()
    message = f'Hello {name}! My name is {hostname}.'
    response = f'{{ message: "{message}" }}\r\n'
    code = 200
    return response, code,  {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# EOF
