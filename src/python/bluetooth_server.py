import bluetooth as bt
import time

def connect(addr=None, name=None):
	'''
	This fuction is used to establish a connection between the computer and device.
	addr is the MAC address of the bt chip, name is name of the device
	specify either one to connect to the device, specifing addr is much faster
 	returns a socket object, which has a stream to the device
	'''
	devs = bt.discover_devices()
	#returns a list of addresses of visible bluetooth devices
	if addr and addr in devs:
		pass
		
	elif name:
		for dev in devs:
			if name == bt.lookup_name( dev ):
				addr = dev
				
	else : return None

	port = 1
	sock=bt.BluetoothSocket( bt.RFCOMM )
	sock.connect((addr, port))
	
	return sock

def servo_sweep(con, init, final, step=1):
	'''
	Test function to sweep servo.
	moves it from 'init thru final' in angle of step
	'''
	con.send(chr(init))
	if step < 1: step = 1
	if init < final:
		sweep = range(init, final, int(step))
	else:
		sweep = range(final, init, int(step))
		sweep.reverse()
		
	for angle in sweep:
		con.send(chr(angle))
		time.sleep(0.02)

	

def main(con):
	try:
		while True:
			servo_sweep(con, 0, 180)
			time.sleep(1)
			servo_sweep(con, 180, 0)
	
	except KeyboardInterrupt as e:
		print "Closing Connection"
		con.close()
		print "Good Bye!! hum hain rahi nerd ke, phir melange chalte chalte" #hindi 
		
if __name__ == '__main__':
	connection = connect(addr = '00:12:12:24:16:30')
	main(connection)

