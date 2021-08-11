from flask import Flask, request
import json
import time


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/upload', methods=[ 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt') 


@app.route('/gettest/<path:subpath>')
def gettest(subpath):
    out = {"subpath": subpath }
    return json.dumps(out, ensure_ascii = False)



if __name__ == '__main__':
    app.run()
