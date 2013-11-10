import bluetooth as bt
import time

name = 'Procebo35'
#name of the bluetooth module on the robotic arm

addr = None
#unique 48 bit address of the bluetooth module (JY MCu)

devs = bt.discover_devices()
#returns a list of addresses of visible bluetooth devices

for dev in devs:
	if name == bt.lookup_name( dev ):
		addr = dev
#now addr has the address of the requirde device (i.e.) our arm

port = 1
sock=bt.BluetoothSocket( bt.RFCOMM )
sock.connect((addr, port))
print 'connected'
sock.send('1')
print 'sent 1'
time.sleep(3)
sock.send('0')
print 'sent 0'
sock.close()
