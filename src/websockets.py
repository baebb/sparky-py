from controller import execute_control

from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory
from pubnub.pubnub import PubNub

pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-86d77efa-af69-435d-bd9d-d9e25341436f"
pnconfig.subscribe_key = "sub-c-3e91234c-012f-11e9-a399-32ec39b2e34f"
pnconfig.ssl = False
pnconfig.uuid = 'droneboi'

pubnub = PubNub(pnconfig)

class WebsocketListener(SubscribeCallback):
    def status(self, pubnub, status):
        # The status object returned is always related to subscribe but could contain
        # information about subscribe, heartbeat, or errors
        # use the operationType to switch on different options
        if status.operation == PNOperationType.PNSubscribeOperation:
            if status.category == PNStatusCategory.PNConnectedCategory:
                print('connected to channel')
            elif status.category == PNStatusCategory.PNReconnectedCategory:
                print('reconnected to channel')
            elif status.category == PNStatusCategory.PNDisconnectedCategory:
                print('disconnected from channel')
            elif status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
                print('unexpected disconnect from channel, retrying')
            elif status.category == PNStatusCategory.PNAccessDeniedCategory:
                print('access to channel denied')
            else:
                print('something else')
        elif status.operation == PNOperationType.PNUnsubscribeOperation:
            print('disconnected from channel')
        elif status.operation == PNOperationType.PNSubscribeOperation:
            if status.is_error():
                print('error connecting to channel')
        else:
            print('something else occured')

    def presence(self, pubnub, presence):
        pass  # handle incoming presence data

    def message(self, pubnub, message):
        if 'control' in message.message:
            new_command = message.message['control']
            execute_control(new_command)

websocket_listener = WebsocketListener()
pubnub.add_listener(websocket_listener)

def connect(channel):
    pubnub.subscribe().channels(channel).execute()

def disconnect():
    pubnub.unsubscribe_all()