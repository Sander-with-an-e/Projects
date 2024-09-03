#Pressure p0 is sea level pressure in Pa
#Pressure p is pressure at input altitude in Pa
#pressure pp is pressure percentage of input altitude wrt sea level in %
#Temperature T0 is sea level temperature in K
#Temperature T is temperature at input altitude in K
#Temperature TC is temperature at input altitude in C
#density rho0 is sea level density in kg/m**3
#density rho is density at input altitude in kg/m**3
#density rhop is density percentage of input altitude wrt sea level in %
#altitude h0 is sea level in m
#altitude h is input altitude in m

import math 

h=float(input('Enter altitude [m]: '))

g0=9.80665 #[m/s^2]
R=287.0 #[J/kgK]
h0=0 #[m]
p0=101325.0 #[Pa]
T0=288.15 #[K]
rho0=p0/(R*T0) #[kg/m^3]

h1=min(h,11000.0)
h2=min(h,20000.0)
h3=min(h,32000.0)
h4=min(h,47000.0)
h5=min(h,51000.0)
h6=min(h,71000.0)
h7=min(h,86000.0)

a1=-0.0065
a2=0
a3=0.0010
a4=0.0028
a5=0
a6=-0.0028
a7=-0.0020

T1=T0+a1*(h1-h0)
T2=T1
T3=T2+a3*(h3-h2)
T4=T3+a4*(h4-h3)
T5=T4
T6=T5+a6*(h6-h5)
T7=T6+a7*(h7-h6)

p1=p0*((T1/T0)**(-g0/(a1*R)))
p2=p1*math.exp((-g0/(R*T2))*(h2-h1))
p3=p2*((T3/T2)**(-g0/(a3*R)))
p4=p3*((T4/T3)**(-g0/(a4*R)))
p5=p4*math.exp((-g0/(R*T5))*(h5-h4))
p6=p5*((T6/T5)**(-g0/(a6*R)))
p7=p6*((T7/T6)**(-g0/(a7*R)))

if h<=11000.0 and h>=0.0:
    T=T1
    p=p1
elif h>11000.0 and h<=20000.0:
    T=T2
    p=p2
elif h>20000.0 and h<=32000.0:
    T=T3
    p=p3
elif h>32000.0 and h<=47000.0:
    T=T4
    p=p4
elif h>47000.0 and h<=51000.0:
    T=T5
    p=p5
elif h>51000.0 and h<=71000.0:
    T=T6
    p=p6
elif h>71000.0 and h<=86000.0:
    T=T7
    p=p7
 
if 0.0<=h and h<=86000.0:
    rho=p/(R*T)
    TC=T-273.15
    pp=(p/p0)*100
    rhop=(rho/rho0)*100
    print('Temperature:',round(T,2),'K', '(',round(TC,1),'C)')
    print('Pressure:',int(p),'Pa','(',int(pp),'% SL)')
    print('Density:',round(rho,4),'kg/m3','(',int(rhop),'% SL)')
else: print('Sorry, I can only do altitudes between 0 m and 86,000 m.')

print('\nReady.')
