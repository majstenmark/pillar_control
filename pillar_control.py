'''
This python 3 (works also with python 2) script is for controlling 
the camera-holding pillar in 
the project Kirurgens perspektiv (Surgeon's perspective). It converts
desired pillar position (level) to the corresponding voltage, which 
should be applied on the internal controller of the pillar.

It is based on the data sheet of the pillar.

IMPORTANT: Position is given in mm.
The voltages are in volts.

About the pillar: 
LC3 pillar, commonly used to adjust the level on desks.
https://www.linak.se/produkter/lyftpelare/lc3/

Manufacturer: LINAK Scandinavia AB
Our contact: Fredrik Strandahl, Försäljningsingenjör
(fredrik.strandahl@linak.se)

Payload: 4000 N
For more data see program variables below.
'''

max_position = 700 # Given in mm.
min_poistion = 0 # All positions are given in mm.
potentiometer_ratio = 0.05 # Potentiometer is 5 % of full scale.

# SUPPLY VOLTAGE MAY BE CHANGED:
supply_voltage = 10.0 # Following the data sheet example, supply voltage is 10 V.
# Ensure this is a float if you use python 2.

pitch = 20.0 # 20. For our pillar that has 4000 N payload. This is (position in mm)/(motor revolutions).
divisor = 62.83 # This is a divisor in the data sheet, without obvious physical interpretation.

def position_reference_to_voltage(position_reference):
    '''
    This function converts desired position of the pillar to
    the corresponding voltage to apply. It returns the voltage v_out.
    '''
    v_out = potentiometer_ratio * supply_voltage +\
    position_reference * float(supply_voltage) / (pitch * divisor)
    return v_out

# For testing. Should evaluate to 3.68 V if supply_voltage is 10.0.
print(position_reference_to_voltage(400)) 
