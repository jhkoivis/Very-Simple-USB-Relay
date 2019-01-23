

import hid

idVendor    = 0x16c0
idProduct   = 0x05df 


relay_1_on_msg = [0xFD, 1]
relay_2_on_msg = [0xFD, 2]

print hid.enumerate(idVendor, idProduct)

h1 = hid.device()
h1.open_path('0001:0008:00')
h1.set_nonblocking(1)
h1.send_feature_report(relay_1_on_msg)


h2 = hid.device()
h2.open_path('0001:0007:00')
h2.set_nonblocking(1)
h2.send_feature_report(relay_2_on_msg)









