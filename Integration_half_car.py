from Eq_half_car import f
import math as m
from scipy.integrate import ode
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from Plot_solar_pre import preprocess
from Plot_solar import animate
from matplotlib.animation import PillowWriter

## Arrays initializations
t_sim = []
x1 = []
x1_dot = []
x2 = []
x2_dot = []
x3 = []
x3_dot = []
x4 = []
x4_dot = []
Front_exct_num = []
Front_exct = []
Rear_exct = []
time_road = []

n = 0

## Importing road profiles
plik = open("Front road.txt", "r")
for line in plik:
    Front_exct_num.append(n)
    line = line.strip()
    Front_exct.append(float(line))
    n = n+1
plik.close()
n = []



## System parameters
MRf=0.6   #Motion ratio front wheel
MRr=0.6   #Motion ratio rear wheel
m1f=20    #Half front unsprung mass
m1r=20    #Half rear unsprung mass
m2=(316/2)-m1f-m1r+140  #Half sprung mass
kt=200000     #Tyre vertical stiffnes
ksr=38000     #Rear suspension spring
kr=ksr*pow(MRr,2)  #Rear suspension vertical stiffness
ksf=32000      #Front suspension spring
kf=ksf*pow(MRf,2)  #Front suspension vertical stiffness
cdr=1500       #Rear damper
cr=cdr*pow(MRr,2)  #Rear vertical damping
cdf=2000      #Front damper
cf=cdf*pow(MRf,2)  #Front vertical damping
lr=1.189    #Distance from front axle to GC %1189/1000;
lf=1.411    #Distance from rear axle to GC %1411/1000
L=lr+lf         #Wheel base
J=m2*lf*lr      #Car moment of inertia  

# Critical damping
ckr=2*m.sqrt(kr*m2)
cpass=0.2*ckr
g=9.81

# Velocity 
v = 80

## Initial conditions
y0 = [-(m2+m1f)*10*lr/(kt*L), 0.0, -(m2+m1r)*10*lf/(kt*L), 0.0, -0.1, 0.0, 0.0, 0.0]
t0 = 0
tk = 10
dt = 0.01 

## Inteprolating road profile so it fits the integration time scale
Front_exct_num_new = [x*tk/Front_exct_num[-1] for x in Front_exct_num]
road_func = interp1d(Front_exct_num_new,Front_exct,fill_value='extrapolate')

r = ode(f).set_integrator('dopri5')
r.set_initial_value(y0,t0).set_f_params(kf, lf, kt, cf, m1f,kr, lr, cr, m1r, m2, J, road_func, time_road, 0.20)

while r.successful and r.t <= tk:
    r.integrate(r.t+dt)

    t_sim.append(r.t)
    x1.append(r.y[0])       #Front unsprung mass
    x1_dot.append(r.y[1])
    x2.append(r.y[2])       #Rear unsprung mass         
    x2_dot.append(r.y[3])
    x3.append(r.y[4])       #Body vertical
    x3_dot.append(r.y[5])
    x4.append(r.y[6])       #Body
    x4_dot.append(r.y[7])


plt.plot(t_sim,x4)
#plt.plot(t_sim,x2)
plt.xlabel('t [s]')
plt.legend(["Front wheel disp","Rear wheel disp"])
plt.show()

# Animations

writer = PillowWriter(fps = 30)
roadall = [x*v for x in t_sim]

fig = plt.figure()

#for i in range(len(t_sim)):
#    Body = preprocess()
#    animate(x3[0],Body, lr, lf, x4[i], x3[i], x1[i], x2[i], t_sim[i], road_func(t_sim),roadall, roadall[i])
with writer.saving(fig, "My_gif.gif", 100):
    for i in range(len(t_sim)):
        Body = preprocess()
        animate(x3[0],Body, lr, lf, x4[i], x3[i], x1[i], x2[i], t_sim[i], road_func(t_sim),roadall, roadall[i])
        writer.grab_frame()

