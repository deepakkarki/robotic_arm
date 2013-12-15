from arm import arm
import gtk
from gtk import *


class ArmControl(gtk.Window):

    def __init__(self):
        super(ArmControl, self).__init__()
        self.myarm = arm(addr = '00:12:12:24:16:30')
        #creating the windows
        self.set_title("Serial Controller")
        self.set_size_request(150, 150)
        self.set_position(WIN_POS_CENTER)
        conn = Button("Connect")
        conn.statex = 0
        conn.connect("clicked", self.on_connect)
        fist = Button("FLEX")
        fist.connect("clicked", self.on_flex)
        fist.statex = 1
        
        #creating the required containers
        mainVBox = VBox(False,5)
        self.add(mainVBox)
        mainVBox.pack_start(Label("SERVO CONTROL"), False, 5, 5)
        mainVBox.pack_start(conn,False,5,5)
        mainVBox.pack_start(fist,False,5,5)
        self.connect("destroy", main_quit)
        self.show_all()
        
        
    def on_connect(self,widget):
        if widget.statex == 0:
            self.myarm.connect()
            widget.statex=1
            widget.set_label("connected")
        else: 
            self.myarm.disconnect()
            widget.statex=0
            widget.set_label("connect")
        
    def on_flex(self,widget):
    	if widget.statex:
    	    self.myarm.write(180)
    	    widget.statex = 0
    	else:
    	    self.myarm.write(0)
    	    widget.statex = 1
    	    
    	
ArmControl()
gtk.main()








