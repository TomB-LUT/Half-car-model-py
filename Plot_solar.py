import numpy as np
import matplotlib.pyplot as plt 
import cv2
import math as m


def animate(InitBody, Body_cord, lr, lf, theta, y2, y1f, y1r, time, Exct, roadall, x_road):

    plt.clf()

    
    #Results magnifications
    #theta=2*theta
    #y2=2*y2
    #InitBody=2*InitBody
        
    y2f=y2+theta*lf
    y2r=y2-theta*lr
    #Road calculations
    X_road=[x-x_road+lf for x in roadall]
    Y_road=[x - 0.5 for x in Exct]

    R = [ [m.cos(-theta), -m.sin(-theta)], [m.sin(-theta), m.cos(-theta)] ]
    #print(R)

    for i in range(len(Body_cord[:,1])):
        a_temp = Body_cord[i,:]
        b = np.matmul(a_temp,R)
        Body_cord[i][:] = b 
        Body_cord[i][0] = Body_cord[i][0] -1.62+lf
        Body_cord[i][1] = Body_cord[i][1] +y2-InitBody

    #Rear wheel 
    r=0.3
    th = np.linspace(0,2*np.pi,100)
    Rxunit = r * np.cos(th) - lr+0.01
    Ryunit = r * np.sin(th) - 0.2 + y1r
    plt.plot(Rxunit, Ryunit,'red')
    
    #Front wheel
    Fxunit = r * np.cos(th) + lf+0.00
    Fyunit = r * np.sin(th) - 0.2 + y1f
    plt.plot(Fxunit, Fyunit,'blue')

    plt.text(2,1,"time: "+str(round(time,2)))

    plt.plot(X_road,Y_road,'black')

    Rdiff=-(y2r+0.2625-(-0.2+y1r))
    line_1 = [-lr, -lr-r/4, -lr+r/4, -lr-r/4, -lr+r/4, -lr-r/4, -lr+r/4, -lr-r/4, -lr+r/4, -lr-r/4, -lr]
    line_2 = [-0.2+y1r, -0.2+y1r-Rdiff*0.5/10, -0.2+y1r-Rdiff*2/10, -0.2+y1r-Rdiff*3/10, 
    -0.2+y1r-Rdiff*4/10, -0.2+y1r-Rdiff*5/10, -0.2+y1r-Rdiff*6/10, -0.2+y1r-Rdiff*7/10, 
    -0.2+y1r-Rdiff*8/10, -0.2+y1r-Rdiff*9.5/10, y2r+0.2625]
    plt.plot(line_1,line_2,'red')
    line_1 = []
    line_2 = []

    Fdiff=-(y2f+0.2625-(-0.2+y1f))
    line_1 = [lf, lf-r/4, lf+r/4, lf-r/4, lf+r/4, lf-r/4, lf+r/4, lf-r/4, lf+r/4, lf-r/4, lf]
    line_2 = [-0.2+y1f, -0.2+y1f-Fdiff*0.5/10, -0.2+y1f-Fdiff*2/10, -0.2+y1f-Fdiff*3/10,
    -0.2+y1f-Fdiff*4/10, -0.2+y1f-Fdiff*5/10, -0.2+y1f-Fdiff*6/10, -0.2+y1f-Fdiff*7/10,
    -0.2+y1f-Fdiff*8/10, -0.2+y1f-Fdiff*9.5/10, y2f+0.2625]
    plt.plot(line_1,line_2,'blue')
    line_1 = []
    line_2 = []

    

    plt.plot(Body_cord[:,0],Body_cord[:,1],'black') #Plotting solar silhouette
    plt.scatter(0,y2, c='black')
    plt.axis([-4, 4, -2, 2,])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(0.001)

    

#plt.show()
