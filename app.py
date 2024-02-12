import ssl
from flask import Flask

app = Flask(__name__)

# HTTPS configuration
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

# HTTPS route
@app.route('/secure')
def index():
    return 'Hello, Flask with SSL!'

if __name__ == '__main__':
    # HTTPS server
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=True)
