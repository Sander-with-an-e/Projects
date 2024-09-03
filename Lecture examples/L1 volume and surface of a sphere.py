# Calculate the surface and volume of a sphere
# 1. Ask input from the user on the radius of the sphere
# 2. Calculate the surface of the sphere
# 3. Calculate the volume of the sphere
# 4. Print the result

import math
# 1. Ask input from the user on the radius of the sphere
radius=input('What is the radius of the sphere?')
radius=float(radius)

# 2. Calculate the surface of the sphere
if radius <0:
    print('Negative radius input!')
else: surface=4*math.pi*radius**2

# 3. Calculate the volume of the sphere
if radius >= 0:
    volume=(4/3)*math.pi*radius**3

# 4. Print the result
if radius >= 0:
    print('surface= ',surface,'volume= ',volume)

# Calculate the surface and volume of a sphere
# 1. Ask input from the user on the radius of the sphere
# 2. Calculate the surface of the sphere
# 3. Calculate the volume of the sphere
# 4. Print the result

import math
# 1. Ask input from the user on the radius of the sphere
radius=input('What is the radius of the sphere?')
radius=float(radius)

# 2. Calculate the surface of the sphere
pi=3.14
surface=4*math.pi*radius**2

# 3. Calculate the volume of the sphere
volume=(4/3)*math.pi*radius**3

# 4. Print the result
print('surface= ',surface,'volume= ',volume)

if radius < 0:
    print('Negative radius input!')
else:
    print('OK!')
          
          
