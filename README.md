# 100-Double-Pendulums-and-Lorenz-Attractor
A simulation of 100 double pendulums with very slight differences in initial conditions that tend toward chaos, and a 3D simulation of the Lorenz 3-set system of ODE's that model atmospheric convection

Program demo:


https://user-images.githubusercontent.com/77819050/130059167-c232f7a1-ddeb-4576-91c5-70f19afc7779.mp4






With guidance from https://matplotlib.org/examples/animation/double_pendulum_animated.html and https://scipython.com/blog/the-double-pendulum/, I created a simulation of 100 double pendulums whose angles between each of the two arms of the pendulum differ by 1 ten-millionth of a degree (or 100 nano-degrees) from the angle of the previous pendulum.
For the first few seconds, the 100 pendulums move in seeming unison, but the slight difference in their starting angle measure is magnified over time, and demonstrates a system tending toward chaos/disorder!

 “a butterfly flapping its wings in Brazil can produce a tornado in Texas” - Edward Norton Lorenz
 
 
 
 # Lorenz-Attractor
A 3D simulation of the Lorenz 3-set system of ODEs that model atmospheric convection.

Simulation Demo Video: 



https://user-images.githubusercontent.com/77819050/130301815-715be9f1-d4e5-4659-83b6-a1f8de55987a.mp4



Using the following system of ODEs known as the Lorenz equations, I plot a dynamic solution to the system assuming the same variable values that Lorenz 
himself used in 1963 when he developed this model.

As the plotting progesses, we see the attractor takes the shape of a butterfly. It demonstrates a likeness to order within a dynamical and chaotic system.


The Lorenz equations implemented, along with the assumed values of the system parameters:

![image](https://user-images.githubusercontent.com/77819050/130300425-358fb9cb-8d17-4f66-ab5c-19307e5599aa.png)
![image](https://user-images.githubusercontent.com/77819050/130300537-158dfeb2-538e-4425-a775-73aed0d63453.png)

