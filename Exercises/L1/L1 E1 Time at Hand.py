# User enters a 24 hour time
# Position of hour hand
# Position of minute hand
# Calculate angle between the hands
# Print angle

# User enters a 24 hour time
time=int(input('Enter the time in hhmm format:'))
#alpha = clockwise angle of hour hand with number 12 of the clock
#beta = clockwise angle of minute hand with number 12 of the clock
#angle = angle between the two hands
alpha=float(alpha)
beta=float(beta)
angle=float(angle)

# Position of hour hand

# Position of minute hand    

# Calculate angle between the hands
# Print angle
if 0000 <= time <= 2400:
    if beta > alpha:
        angle=beta-alpha
        print('angle= ',angle)
    if alpha > beta:
        angle=alpha-beta
        print('angle= ',angle)     
else: print('Incorrect value entered')
