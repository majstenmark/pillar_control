from tkinter import *

import curses
import board
import busio
import adafruit_mcp4725

DEFAULT_VOLTAGE = 0 # lift compressed
MAX_VOLTAGE = 1.7
STEP_LEN = 819

cache_fname = '/home/pi/voltage_cache.txt'
def set_cache(voltage):
    open(cache_fname, 'w').write(str(voltage))

def get_cache():
    try:
        volt = float(open(cache_fname, 'r').read())
        return volt
    except:
        return DEFAULT_VOLTAGE


#setup i2c connection and set correct address
i2c = busio.I2C(board.SCL, board.SDA)
dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)



voltage_out = get_cache()

def send_voltage(voltage_out):
    global stdscr
    if voltage_out > MAX_VOLTAGE:
        stdscr.addstr(2, 20, "Value is too large. Choose a value in the range of 0-5")
        return  
    if voltage_out < 0:
        stdscr.addstr(2, 20, "Voltage must be greater than 0")
        return                        
    set_cache(voltage_out)
    try:
        value = int(voltage_out * STEP_LEN)
        dac.raw_value = value  
        stdscr.addstr(2, 20, "Output set to: " + str(value)  + "V                  ")
    except:
        stdscr.addstr(2, 20, "Something went wrong                           ")
        

def onArrowUp(): 
    global voltage_out
    voltage_out -= 0.05
    voltage_out = max(0, voltage_out)
    send_voltage(voltage_out)

def onArrowDown(): 
    global voltage_out
    voltage_out += 0.05
    voltage_out = min(MAX_VOLTAGE, voltage_out)
    send_voltage(voltage_out)



stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,2,"Hit 'q' to quit, control with up, down or left (up)/right(down) on the remote")
stdscr.refresh()

send_voltage(voltage_out)

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

