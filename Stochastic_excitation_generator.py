import sys
import os
import math as m
import random
import numpy as np
import matplotlib.pyplot as plt
path = os.path.abspath("D:/Konrad/")
sys.path.append(path)
from TBU_functions import zapisz_txt

# Vehicle Variables
lr=1.189    #Distance from front axle to GC %1189/1000;
lf=1.411    #Distance from rear axle to GC %1411/1000
L = lr + lf; 

# Variables for road generation
ISOk = 7; # Values For ISO Road A-B Roughness Classification, from 3 to 9
N  = 2500; # Number of data points
RoadL  = 250;  # Length Of Road Profile (m)
B  = L/N ; # Sampling Interval (m)
dn = 1/RoadL;  # Frequency Band
n0 = 0.1;        # Spatial Frequency (cycles/m)
dn_temp = dn
v = 10

# Creating n array
n = []
while dn_temp <= N*dn: 
    n.append(dn_temp)
    dn_temp = dn_temp+dn

# Creating phi array
random.seed(1)
phi = []
for _ in range (len(n)):
    phi_temp = 2*m.pi*random.random()
    phi.append(phi_temp)

# Creating Amp1 array
Amp1 = [m.sqrt(dn)*pow(2,ISOk)*(1e-3)*(n0/x) for x in n]

# Creating x array
x = []
B_temp = 0
while B_temp <=RoadL-B:
    x.append(B_temp)
    B_temp = B_temp+B

# Define time
t0=0
tf = x[-1]/v
delay=L/80

ttf = [x/v for x in x]  
ttr = [x-delay for x in ttf]

hr = np.empty([1,len(ttf)])#zeros(size(x))
hf = np.empty([1,len(ttf)])

for i in range (len(ttf)):
    hr[0,i] = sum( np.array(Amp1) * np.cos( np.array(n) * 2*m.pi * ttr[i] + np.array(phi))) 
    hf[0,i] = sum( np.array(Amp1) * np.cos( np.array(n) * 2*m.pi * ttf[i] + np.array(phi))) 

zapisz_txt(hr[0,:].tolist()," ","Rear road.txt")
zapisz_txt(hf[0,:].tolist(), " ", "Front road.txt")

plt.plot(ttf,hf[0,:])    
plt.plot(ttr,hr[0,:])
plt.show()

#s_time=RoadL/v
#tspan=[t0,tf]
#step=s_time/N*2*2   
