from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/control/start')
def run_start():
    return 'start'

@app.route('/control/stop')
def run_stop():
    return 'stop'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
