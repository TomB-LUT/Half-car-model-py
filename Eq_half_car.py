# Half-car model equations of motion
# Excitation in the form of road profile from file
import math as m 
g = 9.81

def f(t,y, kf, lf, kt, cf, m1f,kr, lr, cr, m1r, m2, J, road_func, time_road_new, w):
    delay = 2.5/80
    Front_exct_temp = road_func(t)
    Rear_exct_temp = road_func(t-delay)


    return [y[1],
            (-kf*(y[0]-y[4]-lf*y[6])-kt*(y[0]-Front_exct_temp)-cf*(y[1]-y[5]-lf*y[7])-m1f*g)/m1f, 
            #(-kf*(y[0]-y[4]-lf*y[6])-kt*(y[0]-0.1*m.sin(w*t))-cf*(y[1]-y[5]-lf*y[7])-m1f*g)/m1f,
            
            y[3],
            (-kr*(y[2]-y[4]+lr*y[6])-kt*(y[2]-Rear_exct_temp)-cr*(y[3]+lr*y[7]-y[5])-m1r*g)/m1r, 
            #(-kr*(y[2]-y[4]+lr*y[6])-kt*(y[2]-0.1*m.sin(w*(t-delay)))-cr*(y[3]+lr*y[7]-y[5])-m1r*g)/m1r,
            
            y[5],
            (-kr*(y[4]-lr*y[6]-y[2])-kf*(y[4]-y[0]+lf*y[6])-cr*(y[5]-lr*y[7]-y[3])-cf*(y[5]-y[1]+lf*y[7])-m2*g)/m2,
            
            y[7],
            (+lr*kr*(y[4]-lr*y[6]-y[2])+lr*cr*(y[5]-lr*y[7]-y[3])-lf*kf*(y[4]+lf*y[6]-y[0])-lf*cf*(y[5]+lf*y[7]-y[1]))/J]
