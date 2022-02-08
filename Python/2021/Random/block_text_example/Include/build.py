# ---<{ Block font test, from figlet    }>---
# ---<{  Coded by: Parker Cranfield     }>---
# ---<{        Jan. 24, 2021            }>---

"""
REFERENCE::

www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/

www.pypi.org/project/pyfiglet/0.7.4/

"""

# IMPORTS
import pyfiglet # Used for the block text

# setup
f = pyfiglet.Figlet(font="slant") # assign a var to the font style
print(f.renderText("text to render")) # turn the text into the desired font