#johanna oday lab7 
#part 1
#1) Individual plots 

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math

import ctypes  # An included library with Python install.
print("for some reason you have to close all of the plot windows for the next block of code to run so do this for each part")

file_data = np.loadtxt('droptower_vdata.txt')
time = file_data[:,0]
velocity = file_data[:,1]
displacement = integrate.cumtrapz(velocity, x= time, dx = 1.0, initial =0)
acceleration = np.diff(velocity)
acceleration = np.insert(acceleration,[0],[0])  #set acceleration to zero at start
print(acceleration)

plt.figure(0)
velocity_plot = plt.plot(time,velocity,'r')
plt.title("Velocity plot")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")


plt.figure(1)
displacement_plot = plt.plot(time,displacement,'b')
plt.title('Displacement plot')
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.savefig('Displacement Plot.png')


#Acceleration
plt.figure(2)
time2 = np.delete(time,0)
#append the time array because ndiff has one less elt since it's
#taking the difference between two points and thus will have n-1 elements of array length n
acceleration_plot = plt.plot(time,acceleration,'g')
plt.title('Acceleration plot')
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s*s)")
plt.savefig('Acceleration Plot.png')

#Show all the plots
plt.show(0)
plt.show(1)
plt.show(2)


#2) All 3 lines on the same pair of axes with legend

plt.figure(3)
plt.plot(time,velocity,'r--',label='Velocity')
plt.plot(time,displacement,'b',label='Displacement')
plt.plot(time,acceleration,'g',label='Acceleration')
plt.title("All of the plots, velocity, displacement and acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m), Velocity (m/s), Acceleration (m/s^2)")
plt.legend()
plt.savefig("All the plots together.png")
plt.show()

#3) All 3 subplots in a figure
f, axarr = plt.subplots(3, sharex=True, sharey=True)
axarr[0].plot(time,velocity,color='r')
axarr[0].set_ylabel("Velocity (m/s)")
axarr[1].plot(time,displacement,color='b')
axarr[1].set_ylabel("Displacement (m)")
axarr[2].plot(time,acceleration,color='g')
f.subplots_adjust(hspace=0.1) 
plt.suptitle("Velocity, displacement and acceleration")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.savefig("Subplots together in a plot.png")
plt.show()
