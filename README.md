# Sine_Lookup_Generator
This Python 3 script generates a single cycle sine wave look up table. It's useful for digital synthesis of sine waves with a DAC.

Invoke the script with a terminal:
```
>python <dir_path>\sine_table.py --size=1024 --floor=0 --ceiling=4095
```
or
```
>python <dir_path>\sine_table.py --s=1024 --f=0 --c=4095
```
Parameter help:
```
>python <dir_path>\sine_table.py -h
```

## Parameters:
* --size : Table size, Integer.
* --floor : Minimum value of the amplitude. Integer (optional, defaults to 0)
* --ceiling : Maximum value of the amplitude. Integer (optional, defaults to 1023)

### Note:
Not all DACs are capable of true Rail-to-Rail outputs.
Use `--ceiling`, `--floor` to adjust the output to avoid clipping/distortion like shown bellow.
```
>python <dir_path>\sine_table.py --s=1024 --f=96 --c=4000
```
