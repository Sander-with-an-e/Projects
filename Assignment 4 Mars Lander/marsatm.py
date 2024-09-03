#def marsinit_1():
#    marstable_1 = []
#    f = open('/TU Delft Aerospace Engineering/Python/projects/Assignment 4 Mars Lander/marsatm.txt', 'r')
#    for line in f:
#        line = line.strip()
#        if line[0] != ' ' and line[0] != '*':
#            data = line.split(' ')
#            height = data[0].strip()
#            temperature = data[1].strip()
#            density = data[2].strip()
#            speed_of_sound = data[3].strip()
#            marstable_1.append([height,temperature,density,speed_of_sound])
#    f.close
#    for sublist in marstable_1:
#        sublist[0] = float(sublist[0])
#        sublist[1] = float(sublist[1])
#        sublist[2] = float(sublist[2])
#        sublist[3] = float(sublist[3])
#    return marstable_1

#marstable_1 = marsinit_1()
#print(marstable_1)



import numpy as np

#read the data file and store the relevant numbers in a table
def marsinit():
    f = open('/TU Delft Aerospace Engineering/Python/projects/Assignment 4 Mars Lander/marsatm.txt', 'r')
    marstable = np.genfromtxt(f, dtype = 'float', comments='**', delimiter=' ', skip_header=2)
    f.close
    return marstable



def marsatm_1(h, marstable):
    #assign the names to each variable in the table
    altitude = marstable[:, 0]
    temperature = marstable[:, 1]
    density = marstable[:, 2]
    speed_of_sound = marstable[:, 3]

    #interpolation of h for different variables
    rho = np.interp(h, altitude, density)
    temp = np.interp(h, altitude, temperature)
    c = np.interp(h, altitude, speed_of_sound)

    return temp, rho, c

    
