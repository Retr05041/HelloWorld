# -- Triangle Arithmagon --
# -- June 24th, 2021 --
# -- Coded by: Parker Cranfield --

x1 = None # Bottom Right
x2 = None # Bottom Left
x3 = None # Top

y1 = 14 # Left
y2 = 8 # Right
y3 = 1 # Bottom

cap = (y1+y2+y3)/2

if cap > y1:
    x1 = cap-y1
else:
    x1 = y1-cap

if cap > y2:
    x2 = cap-y2
else:
    x2 = y2-cap

if cap > y3:
    x3 = cap-y3
else:
    x3 = y3-cap

print(x1, x2, x3)