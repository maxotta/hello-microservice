#
# Hello microservice example.
#

from flask import Flask, jsonify
from OpenSSL import crypto
import socket
import os

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    hostname = socket.gethostname()
    message = f'Hello {name}! My name is {hostname}.'
    response = f'{{ "message": "{message}" }}\r\n'
    code = 200
    return response, code,  {'Content-Type': 'application/json'}

# Dump all environment variables as JSON.
@app.route('/env')
def list_env():
    import os
    env_vars = os.environ
    response = jsonify(env=dict(os.environ))
    code = 200
    return response, code,  {'Content-Type': 'application/json'}

# Dump the certificate '/configuration/Root_CA.pem' in text format.
@app.route('/cert')
def get_certificate():
    from OpenSSL import crypto
    import os
    cert_path = '/configuration/Root_CA.pem'
    if os.path.exists(cert_path):
        with open(cert_path, 'r') as f:
            c = crypto.load_certificate(crypto.FILETYPE_PEM, f.read())
            cert_data = crypto.dump_certificate(crypto.FILETYPE_TEXT, c)
        response = cert_data.decode('utf-8')
        code = 200
        return response, code, {'Content-Type': 'text/plain'}
    else:
        response = f'{{ "error": "Certificate not found" }}\r\n'
        code = 404
        return response, code, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# EOF
