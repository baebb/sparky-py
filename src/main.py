from flask import Flask
# from controller import execute_control
from websockets import connect, disconnect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'dog!'

@app.route('/control/start')
def run_start():
    connect('controls')
    return 'start'

@app.route('/control/stop')
def run_stop():
    disconnect()
    return 'stop'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)