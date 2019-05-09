# Sine Lookup Table Generator
This Python 3 script generates a single cycle sine wave look up table. It's useful for digital synthesis of sine waves with a DAC. Output is formated in hexadecimal with fixed 16 bit width and 16 data points per raw.

Invoke the script with a terminal:
```
>python <dir_path>\sine_lookup_generatore.py --size=1024 --floor=0 --ceiling=4095
```
or
```
>python <dir_path>\sine_lookup_generatore.py --s=1024 --f=0 --c=4095
```
Parameter help:
```
>python <dir_path>\sine_lookup_generatore.py -h
```

## Parameters:
* --size : Table size, Integer.
* --floor : Minimum value of the amplitude. Integer (optional, defaults to 0)
* --ceiling : Maximum value of the amplitude. Integer (optional, defaults to 1023)
## Output:
![Example Output](ExampleOutput.png?raw=true)
### Note:
Not all DACs are capable of true Rail-to-Rail outputs.
Use `--ceiling`, `--floor` to adjust the output to avoid clipping/distortion like shown bellow.
```
>python <dir_path>\sine_lookup_generatore.py --s=1024 --f=95 --c=4000
```
