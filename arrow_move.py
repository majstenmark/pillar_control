from Tkinter import *
import board
import busio
import adafruit_mcp4725


#setup i2c connection and set correct address
i2c = busio.I2C(board.SCL, board.SDA)
dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)



voltage_out = 0

def send_voltage():
    if voltage_out > 5:
        print("Value is too large. Choose a value in the range of 0-5")    
    if voltage_out < 0:
        print("Voltage must be greater than 0")
    else:
        #calculate input range
        calc = float(4095.0 / 5.0)
        dac.raw_value = int(voltage_out * calc)
        print("Output set to: " + str(value) + "V")

send_voltage()

def onArrowUp(event): 
    print 'Got up arrow key press'
    voltage_out -= 0.05
    send_voltage()

def onArrowDown(event): 
    print 'Got down arrow key press'
    voltage_out += 0.05
    send_voltage()

     
tkroot = Tk()
labelfont = ('courier', 20, 'bold')                
widget = Label(tkroot, text='Press arrows to move!')
widget.config(bg='white', font=labelfont)            
widget.config(height=5, width=30)                  
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Up>', onArrowUp)
widget.bind('<Down>', onArrowDown)

widget.focus()                                     
tkroot.title(' ')
tkroot.mainloop()
