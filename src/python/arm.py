import bluetooth as bt
import time

class arm:
	
	def __init__(self, addr='', name=''):
		self.addr = addr
		self.name = name
		self.conn = None
	
	def connect(self):

		devs = bt.discover_devices()
		addr = self.addr
		name = self.name
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
	
		self.conn = sock

	def write(self,val):
	'''
	val is a list of int (in the range 0-255) to be written
	'''
		for val in vals:
			self.conn.send(chr(val))
	
	def disconnect(self):
		self.conn.close()

	if __name__ == '__main__':
		connection = connect(addr = '00:12:12:24:16:30')
		main(connection)
