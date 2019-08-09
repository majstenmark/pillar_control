
import board
import busio
import adafruit_mcp4725


#setup i2c connection and set correct address
i2c = busio.I2C(board.SCL, board.SDA)
dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)

while True:
    #ask user for input value
    value = float(input("Please enter a value: "))
    if value > 5 :
        print("Value is too large. Choose a value in the range of 0-5")    
    else:
        #calculate input range
        calc = float(4095.0 / 5.0)
        dac.raw_value = int(value * calc)
        print("Output set to: " + str(value) + "V")

