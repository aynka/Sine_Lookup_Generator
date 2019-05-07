#This script is tested with Python 3.7
import sys
import math
import argparse

def scale_number(unscaled, to_min, to_max, from_min, from_max):
    val = (to_max-to_min)*(unscaled-from_min)/(from_max-from_min)+to_min
    return round(val)
    
def generate_sine_table(length=1024, maxVal = 1023, minVal = 0):    
    raw_table = []  
    
    for index, item in enumerate((math.sin(2*math.pi*i/length) for i in range(length))):
        #print(scale_number(item, minVal, maxVal, -1, 1))
        if divmod(index+1, 16)[-1]:
           raw_table.append(format(int(scale_number(item, minVal, maxVal, -1, 1)), '#06x'))
        elif (index+1) != length:
           raw_table.append(format(int(scale_number(item, minVal, maxVal, -1, 1)),'#06x')+ ',\n')
        else:
           raw_table.append(format(int(scale_number(item, minVal, maxVal, -1, 1)),'#06x'))
          
    output_table = []    
    for item in (raw_table[j:j+16] for j in range(0, len(raw_table), 16)):
        output_table.append(','.join(item) )
    print (''.join(output_table))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates a lookup table for sine function.')
    parser.add_argument('--size', required=True, type=int, help='Table size')
    parser.add_argument('--ceiling',  type=int, default=1023, help='Maximum amplitude')
    parser.add_argument('--floor',  type=int, default=0, help='Minimum amplitude')
    args = parser.parse_args()
    
    tableLen = args.size    
    minVal = args.floor     
    maxVal = args.ceiling  
    
    print ( 'Table size = ', tableLen, '; Ceiling = ', maxVal, '; Floor = ', minVal)
    generate_sine_table(tableLen, maxVal, minVal)