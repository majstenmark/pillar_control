from tkinter import *
from timeit import default_timer as timer
import curses


#import board
#import busio
#import adafruit_mcp4725


#setup i2c connection and set correct address
#i2c = busio.I2C(board.SCL, board.SDA)
#dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)
last_press = 0

def send_voltage():
    global voltage_out
    global stdscr
    
    if voltage_out > 5:
        stdscr.addstr(2, 20, "Value is too large. Choose a value in the range of 0-5")    
    elif voltage_out < 0:
        stdscr.addstr(2, 20, "Voltage must be greater than 0                           ")
    else:
        try:
            #calculate input range
            calc = float(4095.0 / 5.0)
            dac.raw_value = int(voltage_out * calc)
            value = int(voltage_out * calc)
            
            stdscr.addstr(2, 20, "Output set to: " + str(value) + "V                  ")
        except:
            stdscr.addstr(2, 20, "Something went wrong                       ")

def onArrowUp(): 
    global voltage_out, last_press
    now = timer.time
    if now - last_press < 1:
        return
    voltage_out -= 0.05
    stdscr.addstr(2, 20, "" + str(now))
    voltage = max(0, voltage_out)
    last_press =  timer.time
    #send_voltage()

def onArrowDown(): 
    global voltage_out
    voltage_out += 0.05
    voltage = min(5, voltage_out)
    #send_voltage()

voltage_out = 1


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,2,"Hit 'q' to quit, control with up, down or left (up)/right(down) on the remote")
stdscr.refresh()

#send_voltage()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 20, "Up  ")
        onArrowUp()
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(3, 20, "Down")
        onArrowDown()
    elif key == curses.KEY_RIGHT: 
        stdscr.addstr(3, 20, "Down")
        onArrowDown()
    elif key == curses.KEY_LEFT: 
        stdscr.addstr(3, 20, "Up  ")
        onArrowUp()
    elif key == 338: 
        stdscr.addstr(3, 20, "Down")
        onArrowDown()
    elif key == 339: 
        onArrowUp()
        stdscr.addstr(3, 20, "Up   ")
curses.endwin()







