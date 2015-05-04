__version__ = '0.0.1' #declare the app version. Will be used by buildozer


from kivy.app import App #for the main app
from kivy.uix.floatlayout import FloatLayout #the UI layout
from kivy.uix.label import Label #a label to show information
from plyer import accelerometer #object to read the accelerometer
from kivy.clock import Clock #clock to schedule a method
import datetime

class UI(FloatLayout):#the app ui
        def __init__(self, **kwargs):
                super(UI, self).__init__(**kwargs)
                self.lblAcce = Label(text="Accelerometer: ") #create a label at the center
                self.add_widget(self.lblAcce) #add the label at the screen
                self.f=open("test","a")
                try:
                        accelerometer.enable() 
                except:
                        self.lblAcce.text = "Failed to start accelerometer" #error
                Clock.schedule_interval(self.update, 1.0/200) #24 calls per seconda
                
        def update(self, dt):
                txt = datetime.datetime.now().strftime("%H %M %S ")+str(datetime.datetime.now().microsecond)
                try:
                        txt = txt+" %.2f %.2f %2.f \n" %(
                                accelerometer.acceleration[0], #read the X value
                                accelerometer.acceleration[1], # Y
                                accelerometer.acceleration[2]) # Z
                except:
                        txt = "Cannot read accelerometer!" #error
                self.lblAcce.text = txt #add the correct text 
                self.f.write(txt)
        def save(self):
                self.f.close()

class Accelerometer(App): #our app
        def build(self):
                self.ui = UI()# create the UI
                return self.ui #show it

        def on_stop(self):
                self.ui.save()
            
if __name__ in ('__android__', '__main__'):
    Accelerometer().run()
