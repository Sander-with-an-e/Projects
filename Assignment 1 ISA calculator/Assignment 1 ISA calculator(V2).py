#Pressure p0 is sea level pressure in Pa
#Pressure p is pressure at input altitude in Pa
#pressure pp is pressure percentage of input altitude wrt sea level in %
#Temperature T0 is sea level temperature in K
#Temperature T is temperature at input altitude in K
#Temperature TC is temperature at input altitude in C
#density rho0 is sea level density in kg/m**3
#density rho is density at input altitude in kg/m**3
#density rhop is density percentage of input altitude wrt sea level in %
#altitude h0 is sea level in m, so 0 m
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

if h<=11000.0 and h>=0.0:
    a=-0.0065
    T=T0+a*(h1-h0)
    p=p0*((T/T0)**(-g0/(a*R)))
elif h>11000.0 and h<=20000.0:
    T=216.65
    p1=22625
    p=p1*math.exp((-g0/(R*T))*(h-h1))
elif h>20000.0 and h<=32000.0:
    a=0.0010
    T2=216.15
    p2=5471
    T=T2+a*(h-h2)
    p=p2*((T/T2)**(-g0/(a*R)))
elif h>32000.0 and h<=47000.0:
    a=0.0028
    T3=228.15
    p3=863
    T=T3+a*(h-h3)
    p=p3*((T/T3)**(-g0/(a*R)))
elif h>47000.0 and h<=51000.0:
    T=270.15
    p4=109
    p=p4*math.exp((-g0/(R*T))*(h-h4))
elif h>51000.0 and h<=71000.0:
    a=-0.0028
    T5=270.15
    p5=65
    T=T5+a*(h-h5)
    p=p5*((T/T5)**(-g0/(a*R)))
elif h>71000.0 and h<=86000.0:
    a=-0.0020
    T6=214.15
    p6=3
    T=T6+a*(h-h6)
    p=p6*((T/T6)**(-g0/(a*R)))

if 0<=h and h<=86000:
    rho=p/(R*T)
    TC=T-273.15
    pp=(p/p0)*100
    rhop=(rho/rho0)*100
    print('Temperature:',round(T,2),'K', '(',round(TC,1),'C)')
    print('Pressure:',int(p),'Pa','(',int(pp),'% SL)')
    print('Density:',round(rho,4),'kg/m3','(',int(rhop),'% SL)')
else: print('Sorry, I can only do altitudes between 0 m and 86,000 m.')

print('\nReady.')

