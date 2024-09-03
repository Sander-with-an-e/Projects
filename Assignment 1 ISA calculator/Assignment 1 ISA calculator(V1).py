#Troposphere calculation (h < 11 km)

#Pressure p0 is sea level pressure in Pa
#Pressure p1 is pressure at input altitude in Pa
#pressure pp1 is pressure percentage of input altitude wrt sea level in %
#Temperature T0 is sea level temperature in K
#Temperature T1 is temperature at input altitude in K
#Temperature TC1 is temperature at input altitude in C
#density rho0 is sea level density in kg/m**3
#density rho1 is density at input altitude in kg/m**3
#density rhop1 is density percentage of input altitude wrt sea level in %
#altitude h0 is sea level in m, so 0 m
#altitude h1 is input altitude in m

h1=float(input('Enter altitude [m]: '))

a=-0.0065 #[K/m]
g0=9.80665 #[m/s**2]
R=287.0 #[J/kgK]
h0 = 0 #[m]
p0=101325.0 #[Pa]
T0=288.15 #[K]
rho0=p0/(R*T0) #[kg/m**3]


if h1<=11000 and h1>=0:
    T1=T0+a*(h1-h0)
    p1=p0*((T1/T0)**(-g0/(a*R)))
    rho1=p1/(R*T1)
    TC1=T1-273.15
    pp1=(p1/p0)*100
    rhop1=(rho1/rho0)*100
    print('Temperature:',round(T1,2),'K', '(',round(TC1,1),'C)')
    print('Pressure:',int(p1),'Pa','(',int(pp1),'% SL)')
    print('Density:',round(rho1,4),'kg/m3','(',int(rhop1),'% SL)')
else: print('Sorry, I can only do altitudes up to 11000 m')

print('\nReady.')
