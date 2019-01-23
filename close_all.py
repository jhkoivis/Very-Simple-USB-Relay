

from relay_03 import Relay

relay_07 = Relay(path = '0001:0007:00')
relay_08 = Relay(path = '0001:0008:00')

relay_07.state(0, on=False)
relay_08.state(0, on=False)



