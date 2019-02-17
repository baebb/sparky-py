from serial import Serial

try:
    port = Serial('/dev/ttyACM0')
except:
    print('USB controller not connected')

control_key = {
    'up': 'f',
    'down': 'b',
    'left': 'l',
    'right': 'r',
    'stop': 's'
}

def execute_control(control):
    if control in control_key.keys():
        command = control_key[control]
        port.write(command.encode())
    else:
        print('Command not recognized')