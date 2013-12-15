from arm import arm

myarm = arm(addr = '00:12:12:24:16:30')
myarm.connect()
print "Welcome to the Bluetooth Arm!! \n"

while True:
	try:
		val = int(input("Enter a number between 0-180 : "))
		lval = [val]*5
		myarm.write(lval)
	except KeyboardInterrupt as e:
		print "See you later! goodbye"
		break
		
	except Exception as e:
		print e
		print "something wrong!! was it you input?"
	
myarm.disconnect()
