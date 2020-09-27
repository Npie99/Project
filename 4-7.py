from vpython import *
import math

distance = graph(width=400, height=300, xtitle='time', ytitle='distance')
Xdot = gdots(color=color.green, graph=distance)
Ydot = gdots(color=color.blue, graph=distance)

displacement = graph(width=400, height=300, xtitle='time', ytitle='displacement')
Ddot = gdots(color=color.red, graph=displacement)

rocket = sphere(pos=vector(0, 0, 0),  radius=1, make_trail=True, make_arrow=True)
rocket.velocity = vector(0, 0, 0)

accelerator = 6.00
wind = 1.50
dt = 0.01
t = 0

while t <= 6:
    rate(100)
    rocket.velocity.y = rocket.velocity.y + (accelerator * dt)
    rocket.pos.y = rocket.pos.y + (rocket.velocity.y * dt)
    rocket.velocity.x = rocket.velocity.x + (wind * dt)
    rocket.pos.x = rocket.pos.x + (rocket.velocity.x * dt)
    DPM = math.sqrt(rocket.pos.x ** 2 + rocket.pos.y ** 2 )
    Xdot.plot(t, rocket.pos.x)
    Ydot.plot(t, rocket.pos.y)
    Ddot.plot(t, DPM)
    t = t + dt
    print(DPM)

