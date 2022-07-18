## colors
#### A module for printing colored text easily

The colors.py module contains an Enum class that stores the colors and its values,\
and the cprint() function which prints colored text.

The following is a quick example of how to use it:
```python
from colors import Color, cprint

cprint(Color.blue, 'This color is blue')
```
```
'This color is blue'
```

You can also pass multiple strings, and also keyword arguments
for the standard print() function:
```python
cprint(Color.green, 'This', 'color', 'is', 'green', sep='-', end='\n ----')
```
```
'This-color-is-green
 ----'
```
