from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

@app.route('/api/v1/hello-word-2')
def index():
    return "Hello world 2"

if __name__=="__main__":
    WSGIServer(('', 5000), app).serve_forever()
