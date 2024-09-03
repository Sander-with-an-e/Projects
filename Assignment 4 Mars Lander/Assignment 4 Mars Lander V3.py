import math
import matplotlib.pyplot as plt
import numpy as np


def run_simulation(hT, m_fuel):
    g0 = -3.711 # m/s^2
    ve = 4400 # m/s
    kv = 0.05
    CdS = 4.92 # m^2

    m_zfw = 699.0 # kg
    m = m_zfw + m_fuel # kg

    gamma = -20 # deg

    v = 262.0 # m/s
    vx = math.cos(math.radians(gamma)) * v # m/s
    vy = math.sin(math.radians(gamma)) * v # m/s
    vy_ref = -2.0 # m/s

    h = 20 # km
    x = 0 # km

    t = 0 # s
    dt = 0.1 # s

    from marsatm import marsinit, marsatm_1
    marstable = marsinit()

    while True:
        temp, rho, c = marsatm_1(h, marstable)

        if vx == 0:
            gamma = -90
        else:
            gamma = math.degrees(math.atan(vy / vx))

        if h < hT and h > 0.0003 and m_fuel > 0:
            dvy = vy_ref - vy
            m_dot = min(5, ((m * -g0) / ve) + kv * dvy)

            Tx = -m_dot * ve * math.cos(math.radians(gamma))
            Ty = -m_dot * ve * math.sin(math.radians(gamma))

            m_fuel -= m_dot * dt
        else:
            m_dot = 0
            Tx = 0
            Ty = 0

        Fy_g = m * g0
        Fx_drag = -CdS * 0.5 * rho * (v ** 2) * math.cos(math.radians(gamma))
        Fy_drag = -CdS * 0.5 * rho * (v ** 2) * math.sin(math.radians(gamma))

        Fx_tot = Fx_drag + Tx
        Fy_tot = Fy_drag + Ty + Fy_g

        ax = Fx_tot / m
        ay = Fy_tot / m

        vx += ax * dt
        vy += ay * dt
        v = math.sqrt(vx ** 2 + vy ** 2)

        x += (vx / 1000) * dt
        h += (vy / 1000) * dt

        m = m_zfw + m_fuel

        if h <= 0:
            break

        t += dt

    return vy

# Grid search for optimal hT and m_fuel
best_hT = None
best_m_fuel = None
min_vy_final = float('inf')

for hT_test in np.arange(5, 15, 0.5): # km
    for m_fuel_test in np.arange(100, 400, 10): # kg
        vy_final = run_simulation(hT_test, m_fuel_test)
        if vy_final <= 3 and abs(vy_final) < abs(min_vy_final):
            min_vy_final = vy_final
            best_hT = hT_test
            best_m_fuel = m_fuel_test

print(f"Optimal hT: {best_hT} km, Optimal m_fuel: {best_m_fuel} kg, Final vy: {min_vy_final} m/s")
