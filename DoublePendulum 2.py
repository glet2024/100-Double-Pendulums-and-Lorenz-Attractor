from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G =  9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg

#This is helper code that models the physics of a double pendulum at any given state and point in time
#Borrowed from https://matplotlib.org/examples/animation/double_pendulum_animated.html
def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
               M2*G*sin(state[2])*cos(del_) +
               M2*L2*state[3]*state[3]*sin(del_) -
               (M1 + M2)*G*sin(state[0]))/den1

    dydx[2] = state[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
               (M1 + M2)*G*sin(state[0])*cos(del_) -
               (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[2]))/den2

    return dydx

dt = 0.05 #represents the change in time between each frame
duration = 45 #represents the duration of the simulation
t = np.arange(0.0, duration, dt) #sets the time variable


# w1 and w2 are the initial angular velocities (degrees per second)
# th1 >= 79.15 for divergence
th1 =95 #initial degree value of first arm
th2 = 120 #initial degree value of second arm

w1 = 0.0 #initial angular velocitiy of first arm
w2 = 0.0 #initial angular velocity of second arm

angVelAdd = .0000001 #represnts how much our initial angle velocity will differ

# initial states
state = np.radians([th1, w1, th2, w2+.0000001])
state2 = np.radians([th1, w1, th2, w2+.0000002])
state3 = np.radians([th1, w1, th2, w2+.0000003])
state4 = np.radians([th1, w1, th2, w2+.0000004])
state5 = np.radians([th1, w1, th2, w2+.0000005])
state6 = np.radians([th1, w1, th2, w2+.0000006])
state7 = np.radians([th1, w1, th2, w2+.0000007])
state8 = np.radians([th1, w1, th2, w2+.0000008])
state9 = np.radians([th1, w1, th2, w2+.0000009])
state10 = np.radians([th1, w1, th2, w2+.000001])
state11 = np.radians([th1, w1, th2, w2+.0000011])
state12 = np.radians([th1, w1, th2, w2+.0000012])
state13 = np.radians([th1, w1, th2, w2+.0000013])
state14 = np.radians([th1, w1, th2, w2+.0000014])
state15 = np.radians([th1, w1, th2, w2+.0000015])
state16 = np.radians([th1, w1, th2, w2+.0000016])
state17 = np.radians([th1, w1, th2, w2+.0000017])
state18 = np.radians([th1, w1, th2, w2+.0000018])
state19 = np.radians([th1, w1, th2, w2+.0000019])
state20 = np.radians([th1, w1, th2, w2+.000002])
state21 = np.radians([th1, w1, th2, w2+.0000021])
state22 = np.radians([th1, w1, th2, w2+.0000022])
state23 = np.radians([th1, w1, th2, w2+.0000023])
state24 = np.radians([th1, w1, th2, w2+.0000024])
state25 = np.radians([th1, w1, th2, w2+.0000025])
state26 = np.radians([th1, w1, th2, w2+.0000026])
state27 = np.radians([th1, w1, th2, w2+.0000027])
state28 = np.radians([th1, w1, th2, w2+.0000028])
state29 = np.radians([th1, w1, th2, w2+.0000029])
state30 = np.radians([th1, w1, th2, w2+.0000030])
state31 = np.radians([th1, w1, th2, w2+.0000031])
state32 = np.radians([th1, w1, th2, w2+.0000032])
state33 = np.radians([th1, w1, th2, w2+.0000033])
state34 = np.radians([th1, w1, th2, w2+.0000034])
state35 = np.radians([th1, w1, th2, w2+.0000035])
state36 = np.radians([th1, w1, th2, w2+.0000036])
state37 = np.radians([th1, w1, th2, w2+.0000037])
state38 = np.radians([th1, w1, th2, w2+.0000038])
state39 = np.radians([th1, w1, th2, w2+.0000039])
state40 = np.radians([th1, w1, th2, w2+.0000040])

# integrate your ODE using scipy.integrate.
a = integrate.odeint(derivs, state, t)
b = integrate.odeint(derivs, state2, t)
c = integrate.odeint(derivs, state3, t)
d = integrate.odeint(derivs, state4, t)
e = integrate.odeint(derivs, state5, t)
f = integrate.odeint(derivs, state6, t)
g = integrate.odeint(derivs, state7, t)
h = integrate.odeint(derivs, state8, t)
i = integrate.odeint(derivs, state9, t)
j = integrate.odeint(derivs, state10, t)
k = integrate.odeint(derivs, state11, t)
l = integrate.odeint(derivs, state12, t)
m = integrate.odeint(derivs, state13, t)
n = integrate.odeint(derivs, state14, t)
o = integrate.odeint(derivs, state15, t)
p = integrate.odeint(derivs, state16, t)
q = integrate.odeint(derivs, state17, t)
r = integrate.odeint(derivs, state18, t)
s = integrate.odeint(derivs, state19, t)
t = integrate.odeint(derivs, state20, t)
t = np.arange(0.0, duration, dt)
aa = integrate.odeint(derivs, state21, t)
bb = integrate.odeint(derivs, state22, t)
cc = integrate.odeint(derivs, state23, t)
dd = integrate.odeint(derivs, state24, t)
ee = integrate.odeint(derivs, state25, t)
ff = integrate.odeint(derivs, state26, t)
gg = integrate.odeint(derivs, state27, t)
hh = integrate.odeint(derivs, state28, t)
ii = integrate.odeint(derivs, state29, t)
jj = integrate.odeint(derivs, state30, t)
kk = integrate.odeint(derivs, state31, t)
ll = integrate.odeint(derivs, state32, t)
mm = integrate.odeint(derivs, state33, t)
nn = integrate.odeint(derivs, state34, t)
oo = integrate.odeint(derivs, state35, t)
pp = integrate.odeint(derivs, state36, t)
qq = integrate.odeint(derivs, state37, t)
rr = integrate.odeint(derivs, state38, t)
ss = integrate.odeint(derivs, state39, t)
tt = integrate.odeint(derivs, state40, t)

'''
Here, we set pendulum conditions for the first 40 pendulums
'''
x1 = L1 * sin(a[:, 0])
y1 = -L1 * cos(a[:, 0])
x2 = L2 * sin(a[:, 2]) + x1
y2 = -L2 * cos(a[:, 2]) + y1

x21 = L1 * sin(b[:, 0])
y21 = -L1 * cos(b[:, 0])
x22 = L2 * sin(b[:, 2]) + x21
y22 = -L2 * cos(b[:, 2]) + y21

x31 = L1 * sin(c[:, 0])
y31 = -L1 * cos(c[:, 0])
x32 = L2 * sin(c[:, 2]) + x31
y32 = -L2 * cos(c[:, 2]) + y31

x41 = L1 * sin(d[:, 0])
y41 = -L1 * cos(d[:, 0])
x42 = L2 * sin(d[:, 2]) + x41
y42 = -L2 * cos(d[:, 2]) + y41

x51 = L1 * sin(e[:, 0])
y51 = -L1 * cos(e[:, 0])
x52 = L2 * sin(e[:, 2]) + x51
y52 = -L2 * cos(e[:, 2]) + y51

x61 = L1 * sin(f[:, 0])
y61 = -L1 * cos(f[:, 0])
x62 = L2 * sin(f[:, 2]) + x61
y62 = -L2 * cos(f[:, 2]) + y61

x71 = L1 * sin(g[:, 0])
y71 = -L1 * cos(g[:, 0])
x72 = L2 * sin(g[:, 2]) + x71
y72 = -L2 * cos(g[:, 2]) + y71

x81 = L1 * sin(h[:, 0])
y81 = -L1 * cos(h[:, 0])
x82 = L2 * sin(h[:, 2]) + x81
y82 = -L2 * cos(h[:, 2]) + y81

x91 = L1 * sin(i[:, 0])
y91 = -L1 * cos(i[:, 0])
x92 = L2 * sin(i[:, 2]) + x91
y92 = -L2 * cos(i[:, 2]) + y91

x111 = L1 * sin(j[:, 0])
y111 = -L1 * cos(j[:, 0])
x112 = L2 * sin(j[:, 2]) + x111
y112 = -L2 * cos(j[:, 2]) + y111

x121 = L1 * sin(k[:, 0])
y121 = -L1 * cos(k[:, 0])
x122 = L2 * sin(k[:, 2]) + x121
y122 = -L2 * cos(k[:, 2]) + y121

x131 = L1 * sin(l[:, 0])
y131 = -L1 * cos(l[:, 0])
x132 = L2 * sin(l[:, 2]) + x131
y132 = -L2 * cos(l[:, 2]) + y131

x141 = L1 * sin(m[:, 0])
y141 = -L1 * cos(m[:, 0])
x142 = L2 * sin(m[:, 2]) + x141
y142 = -L2 * cos(m[:, 2]) + y141

x151 = L1 * sin(n[:, 0])
y151 = -L1 * cos(n[:, 0])
x152 = L2 * sin(n[:, 2]) + x151
y152 = -L2 * cos(n[:, 2]) + y151

x161 = L1 * sin(o[:, 0])
y161 = -L1 * cos(o[:, 0])
x162 = L2 * sin(o[:, 2]) + x161
y162 = -L2 * cos(o[:, 2]) + y161

x171 = L1 * sin(p[:, 0])
y171 = -L1 * cos(p[:, 0])
x172 = L2 * sin(p[:, 2]) + x171
y172 = -L2 * cos(p[:, 2]) + y171

x181 = L1 * sin(q[:, 0])
y181 = -L1 * cos(q[:, 0])
x182 = L2 * sin(q[:, 2]) + x181
y182 = -L2 * cos(q[:, 2]) + y181

x191 = L1 * sin(r[:, 0])
y191 = -L1 * cos(r[:, 0])
x192 = L2 * sin(r[:, 2]) + x191
y192 = -L2 * cos(r[:, 2]) + y191

x201 = L1 * sin(s[:, 0])
y201 = -L1 * cos(s[:, 0])
x202 = L2 * sin(s[:, 2]) + x201
y202 = -L2 * cos(s[:, 2]) + y201

x211 = L1 * sin(tt[:, 0])
y211 = -L1 * cos(tt[:, 0])
x212 = L2 * sin(tt[:, 2]) + x211
y212 = -L2 * cos(tt[:, 2]) + y211

x1a = L1 * sin(aa[:, 0])
y1a = -L1 * cos(aa[:, 0])
x2a = L2 * sin(aa[:, 2]) + x1a
y2a = -L2 * cos(aa[:, 2]) + y1a

x21b = L1 * sin(bb[:, 0])
y21b = -L1 * cos(bb[:, 0])
x22b = L2 * sin(bb[:, 2]) + x21b
y22b = -L2 * cos(bb[:, 2]) + y21b

x31c = L1 * sin(cc[:, 0])
y31c = -L1 * cos(cc[:, 0])
x32c = L2 * sin(cc[:, 2]) + x31c
y32c = -L2 * cos(cc[:, 2]) + y31c

x41d = L1 * sin(dd[:, 0])
y41d = -L1 * cos(dd[:, 0])
x42d = L2 * sin(dd[:, 2]) + x41d
y42d = -L2 * cos(dd[:, 2]) + y41d

x51e = L1 * sin(ee[:, 0])
y51e = -L1 * cos(ee[:, 0])
x52e = L2 * sin(ee[:, 2]) + x51e
y52e = -L2 * cos(ee[:, 2]) + y51e

x61f = L1 * sin(ff[:, 0])
y61f = -L1 * cos(ff[:, 0])
x62f = L2 * sin(ff[:, 2]) + x61f
y62f = -L2 * cos(ff[:, 2]) + y61f

x71g = L1 * sin(gg[:, 0])
y71g = -L1 * cos(gg[:, 0])
x72g = L2 * sin(gg[:, 2]) + x71g
y72g = -L2 * cos(gg[:, 2]) + y71g

x81h = L1 * sin(hh[:, 0])
y81h = -L1 * cos(hh[:, 0])
x82h = L2 * sin(hh[:, 2]) + x81h
y82h = -L2 * cos(hh[:, 2]) + y81h

x91i = L1 * sin(ii[:, 0])
y91i = -L1 * cos(ii[:, 0])
x92i = L2 * sin(ii[:, 2]) + x91i
y92i = -L2 * cos(ii[:, 2]) + y91i

x111j = L1 * sin(jj[:, 0])
y111j = -L1 * cos(jj[:, 0])
x112j = L2 * sin(jj[:, 2]) + x111j
y112j = -L2 * cos(jj[:, 2]) + y111j

x121k = L1 * sin(kk[:, 0])
y121k = -L1 * cos(kk[:, 0])
x122k = L2 * sin(kk[:, 2]) + x121k
y122k = -L2 * cos(kk[:, 2]) + y121k

x131l = L1 * sin(ll[:, 0])
y131l = -L1 * cos(ll[:, 0])
x132l = L2 * sin(ll[:, 2]) + x131l
y132l = -L2 * cos(ll[:, 2]) + y131l

x141m = L1 * sin(mm[:, 0])
y141m = -L1 * cos(mm[:, 0])
x142m = L2 * sin(mm[:, 2]) + x141m
y142m = -L2 * cos(mm[:, 2]) + y141m

x151n = L1 * sin(nn[:, 0])
y151n = -L1 * cos(nn[:, 0])
x152n = L2 * sin(nn[:, 2]) + x151n
y152n = -L2 * cos(nn[:, 2]) + y151n

x161o = L1 * sin(oo[:, 0])
y161o = -L1 * cos(oo[:, 0])
x162o = L2 * sin(oo[:, 2]) + x161o
y162o = -L2 * cos(oo[:, 2]) + y161o

x171p = L1 * sin(pp[:, 0])
y171p = -L1 * cos(pp[:, 0])
x172p = L2 * sin(pp[:, 2]) + x171p
y172p = -L2 * cos(pp[:, 2]) + y171p

x181q = L1 * sin(qq[:, 0])
y181q = -L1 * cos(qq[:, 0])
x182q = L2 * sin(qq[:, 2]) + x181q
y182q = -L2 * cos(qq[:, 2]) + y181q

x191r = L1 * sin(rr[:, 0])
y191r = -L1 * cos(rr[:, 0])
x192r = L2 * sin(rr[:, 2]) + x191r
y192r = -L2 * cos(rr[:, 2]) + y191r

x201s = L1 * sin(ss[:, 0])
y201s = -L1 * cos(ss[:, 0])
x202s = L2 * sin(ss[:, 2]) + x201s
y202s = -L2 * cos(ss[:, 2]) + y201s

x211t = L1 * sin(tt[:, 0])
y211t = -L1 * cos(tt[:, 0])
x212t = L2 * sin(tt[:, 2]) + x211t
y212t = -L2 * cos(tt[:, 2]) + y211t

x1List = [0] * 60
y1List = [0] * 60
x2List = [0] * 60
y2List = [0] * 60
angVelAdd = .0000001

#handles the state creation of the last 60 pendulums
for _ in range(0, 60):
    stateLoop = np.radians([th1, w1, th2, w2 + .0000040 + angVelAdd])
    # integrate your ODE using scipy.integrate.
    zz = integrate.odeint(derivs, stateLoop, t)

    x1Loop = L1 * sin(zz[:, 0])
    y1Loop = -L1 * cos(zz[:, 0])
    x2Loop = L2 * sin(zz[:, 2]) + x1Loop
    y2Loop = -L2 * cos(zz[:, 2]) + y1Loop

    x1List[_] = x1Loop
    y1List[_] = y1Loop
    x2List[_] = x2Loop
    y2List[_] = y2Loop

    angVelAdd += .0000001 #increment the added degree measure to ensure a minute difference
                          #in every pendulum's starting conditions


size = L1 + L2 #size of our view/simulation is set here

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(xlim=(-size, size), ylim=(-size, size))


ax.set_facecolor('#000000')  # plot color
fig.patch.set_facecolor('#000000')  # border color

#creating each pendulum and assigning it a unique color and a uniform thickness
line, = ax.plot([], [], '-', c='#CFE1EE', lw=2)
line2, = ax.plot([], [], '-', c='#CBE0EF', lw=2)
line3, = ax.plot([], [], '-', c='#C6DEEF', lw=2)
line4, = ax.plot([], [], '-', c='#C1DCEF', lw=2)
line5, = ax.plot([], [], '-', c='#BAD8EE', lw=2)
line6, = ax.plot([], [], '-', c='#B4D5ED', lw=2)
line7, = ax.plot([], [], '-', c='#ADD1EC', lw=2)
line8, = ax.plot([], [], '-', c='#A4CBE9', lw=2)
line9, = ax.plot([], [], '-', c='#9DC8E9', lw=2)
line10, = ax.plot([], [], '-', c='#94C3E8', lw=2)
line11, = ax.plot([], [], '-', c='#8FC1E8', lw=2)
line12, = ax.plot([], [], '-', c='#8BBFE8', lw=2)
line13, = ax.plot([], [], '-', c='#81BAE7', lw=2)
line14, = ax.plot([], [], '-', c='#7CB7E6', lw=2)
line15, = ax.plot([], [], '-', c='#75B4E6', lw=2)
line16, = ax.plot([], [], '-', c='#6DAEE2', lw=2)
line17, = ax.plot([], [], '-', c='#68ABE2', lw=2)
line18, = ax.plot([], [], '-', c='#64A9E2', lw=2)
line19, = ax.plot([], [], '-', c='#62A8E2', lw=2)
line20, = ax.plot([], [], '-', c='#5CA5E1', lw=2)
line21, = ax.plot([], [], '-', c='#59A4E2', lw=2)
line22, = ax.plot([], [], '-', c='#4E9CDD', lw=2)
line23, = ax.plot([], [], '-', c='#4998DA', lw=2)
line24, = ax.plot([], [], '-', c='#4694D6', lw=2)
line25, = ax.plot([], [], '-', c='#3F8CCE', lw=2)
line26, = ax.plot([], [], '-', c='#3A84C3', lw=2)
line27, = ax.plot([], [], '-', c='#367EBB', lw=2)
line28, = ax.plot([], [], '-', c='#3278B3', lw=2)
line29, = ax.plot([], [], '-', c='#2F74AD', lw=2)
line30, = ax.plot([], [], '-', c='#2B6EA6', lw=2)
line31, = ax.plot([], [], '-', c='#27679D', lw=2)
line32, = ax.plot([], [], '-', c='#246397', lw=2)
line33, = ax.plot([], [], '-', c='#236194', lw=2)
line34, = ax.plot([], [], '-', c='#205D8F', lw=2)
line35, = ax.plot([], [], '-', c='#1E5989', lw=2)
line36, = ax.plot([], [], '-', c='#1D5786', lw=2)
line37, = ax.plot([], [], '-', c='#1C5482', lw=2)
line38, = ax.plot([], [], '-', c='#1A517E', lw=2)
line39, = ax.plot([], [], '-', c='#174C77', lw=2)
line40, = ax.plot([], [], '-', c='#0F3E64', lw=2)
line41, = ax.plot([], [], '-', c='#0F395C', lw=2)
line42, = ax.plot([], [], '-', c='#10385A', lw=2)
line43, = ax.plot([], [], '-', c='#123858', lw=2)
line44, = ax.plot([], [], '-', c='#133756', lw=2)
line45, = ax.plot([], [], '-', c='#133756', lw=2)
line46, = ax.plot([], [], '-', c='#153754', lw=2)
line47, = ax.plot([], [], '-', c='#1C3E5A', lw=2)
line48, = ax.plot([], [], '-', c='#1F415D', lw=2)
line49, = ax.plot([], [], '-', c='#274D6D', lw=2)
line50, = ax.plot([], [], '-', c='#2B5172', lw=2)
line51, = ax.plot([], [], '-', c='#295072', lw=2)
line52, = ax.plot([], [], '-', c='#2C5374', lw=2)
line53, = ax.plot([], [], '-', c='#305676', lw=2)
line54, = ax.plot([], [], '-', c='#325777', lw=2)
line55, = ax.plot([], [], '-', c='#365B7A', lw=2)
line56, = ax.plot([], [], '-', c='#345C7D', lw=2)
line57, = ax.plot([], [], '-', c='#335F83', lw=2)
line58, = ax.plot([], [], '-', c='#326189', lw=2)
line59, = ax.plot([], [], '-', c='#326189', lw=2)
line60, = ax.plot([], [], '-', c='#326897', lw=2)
line61, = ax.plot([], [], '-', c='#31709B', lw=2)
line62, = ax.plot([], [], '-', c='#2F719E', lw=2)
line63, = ax.plot([], [], '-', c='#2C72A1', lw=2)
line64, = ax.plot([], [], '-', c='#2A73A5', lw=2)
line65, = ax.plot([], [], '-', c='#2874A7', lw=2)
line66, = ax.plot([], [], '-', c='#2874A7', lw=2)
line67, = ax.plot([], [], '-', c='#2479B1', lw=2)
line68, = ax.plot([], [], '-', c='#227BB6', lw=2)
line69, = ax.plot([], [], '-', c='#2782BE', lw=2)
line70, = ax.plot([], [], '-', c='#2B85C0', lw=2)
line71, = ax.plot([], [], '-', c='#2F88C2', lw=2)
line72, = ax.plot([], [], '-', c='#338EC9', lw=2)
line73, = ax.plot([], [], '-', c='#3691CC', lw=2)
line74, = ax.plot([], [], '-', c='#3A94CE', lw=2)
line75, = ax.plot([], [], '-', c='#3F98D2', lw=2)
line76, = ax.plot([], [], '-', c='#429DD8', lw=2)
line77, = ax.plot([], [], '-', c='#45A2DF', lw=2)
line78, = ax.plot([], [], '-', c='#48A5E2', lw=2)
line79, = ax.plot([], [], '-', c='#4CAAE7', lw=2)
line80, = ax.plot([], [], '-', c='#4FABE7', lw=2)
line81, = ax.plot([], [], '-', c='#53ACE6', lw=2)
line82, = ax.plot([], [], '-', c='#57AEE7', lw=2)
line83, = ax.plot([], [], '-', c='#5DB2EB', lw=2)
line84, = ax.plot([], [], '-', c='#61B3EB', lw=2)
line85, = ax.plot([], [], '-', c='#65B5EC', lw=2)
line86, = ax.plot([], [], '-', c='#67B2E6', lw=2)
line87, = ax.plot([], [], '-', c='#6BB3E5', lw=2)
line88, = ax.plot([], [], '-', c='#70B6E7', lw=2)
line89, = ax.plot([], [], '-', c='#74B6E4', lw=2)
line90, = ax.plot([], [], '-', c='#78B7E2', lw=2)
line91, = ax.plot([], [], '-', c='#7DB8E0', lw=2)
line92, = ax.plot([], [], '-', c='#80B8DE', lw=2)
line93, = ax.plot([], [], '-', c='#86BBDE', lw=2)
line94, = ax.plot([], [], '-', c='#8CBCDC', lw=2)
line95, = ax.plot([], [], '-', c='#93BFDD', lw=2)
line96, = ax.plot([], [], '-', c='#98C2DE', lw=2)
line97, = ax.plot([], [], '-', c='#A0C5DE', lw=2)
line98, = ax.plot([], [], '-', c='#A7C8DE', lw=2)
line99, = ax.plot([], [], '-', c='#B2D1E5', lw=2)
line100, = ax.plot([], [], '-', c='#B9D6E9', lw=2)


time_template = ''
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])

    return line, time_text


def animate(i): #here, we set each line's starting data, and return each line as well
    thisa = [0, x1[i], x2[i]]
    thisaa = [0, y1[i], y2[i]]
    line.set_data(thisa, thisaa)

    thisb = [0, x21[i], x22[i]]
    thisbb = [0, y21[i], y22[i]]
    line2.set_data(thisb, thisbb)

    thisc = [0, x31[i], x32[i]]
    thiscc = [0, y31[i], y32[i]]
    line3.set_data(thisc, thiscc)


    thisd = [0, x211[i], x212[i]]
    thisdd = [0, y211[i], y212[i]]
    line4.set_data(thisd, thisdd)

    thise = [0, x41[i], x42[i]]
    thisee = [0, y41[i], y42[i]]
    line5.set_data(thise, thisee)

    thisf = [0, x51[i], x52[i]]
    thisff = [0, y51[i], y52[i]]
    line6.set_data(thisf, thisff)

    thisg = [0, x61[i], x62[i]]
    thisgg = [0, y61[i], y62[i]]
    line7.set_data(thisg, thisgg)

    thish = [0, x71[i], x72[i]]
    thishh = [0, y71[i], y72[i]]
    line8.set_data(thish, thishh)

    thisi = [0, x81[i], x82[i]]
    thisii = [0, y81[i], y82[i]]
    line9.set_data(thisi, thisii)

    thisj = [0, x91[i], x92[i]]
    thisjj = [0, y91[i], y92[i]]
    line10.set_data(thisj, thisjj)

    thisk = [0, x111[i], x112[i]]
    thiskk = [0, y111[i], y112[i]]
    line11.set_data(thisk, thiskk)

    thisl = [0, x121[i], x122[i]]
    thisll = [0, y121[i], y122[i]]
    line12.set_data(thisl, thisll)

    thism = [0, x131[i], x132[i]]
    thismm = [0, y131[i], y132[i]]
    line13.set_data(thism, thismm)

    thisn = [0, x141[i], x142[i]]
    thisnn = [0, y141[i], y142[i]]
    line14.set_data(thisn, thisnn)

    thiso = [0, x151[i], x152[i]]
    thisoo = [0, y151[i], y152[i]]
    line15.set_data(thiso, thisoo)

    thisp = [0, x161[i], x162[i]]
    thispp = [0, y161[i], y162[i]]
    line16.set_data(thisp, thispp)

    thisq = [0, x171[i], x172[i]]
    thisqq = [0, y171[i], y172[i]]
    line17.set_data(thisq, thisqq)

    thisr = [0, x181[i], x182[i]]
    thisrr = [0, y181[i], y182[i]]
    line18.set_data(thisr, thisrr)

    thiss = [0, x191[i], x192[i]]
    thisss = [0, y191[i], y192[i]]
    line19.set_data(thiss, thisss)

    thist = [0, x201[i], x202[i]]
    thistt = [0, y201[i], y202[i]]
    line20.set_data(thist, thistt)

    thisaq = [0, x1a[i], x2a[i]]
    thisaaq = [0, y1a[i], y2a[i]]
    line21.set_data(thisaq, thisaaq)

    thisbq = [0, x21b[i], x22b[i]]
    thisbbq = [0, y21b[i], y22b[i]]
    line22.set_data(thisbq, thisbbq)

    thiscq = [0, x31c[i], x32c[i]]
    thisccq = [0, y31c[i], y32c[i]]
    line23.set_data(thiscq, thisccq)

    thisdq = [0, x211t[i], x212t[i]]
    thisddq = [0, y211t[i], y212t[i]]
    line24.set_data(thisd, thisddq)

    thiseq = [0, x41d[i], x42d[i]]
    thiseeq = [0, y41d[i], y42d[i]]
    line25.set_data(thiseq, thiseeq)

    thisfq = [0, x51e[i], x52e[i]]
    thisffq = [0, y51e[i], y52e[i]]
    line26.set_data(thisfq, thisffq)

    thisgq = [0, x61f[i], x62f[i]]
    thisggq = [0, y61f[i], y62f[i]]
    line27.set_data(thisgq, thisggq)

    thishq = [0, x71g[i], x72g[i]]
    thishhq = [0, y71g[i], y72g[i]]
    line28.set_data(thishq, thishhq)

    thisiq = [0, x81h[i], x82h[i]]
    thisiiq = [0, y81h[i], y82h[i]]
    line29.set_data(thisiq, thisiiq)

    thisjq = [0, x91i[i], x92i[i]]
    thisjjq = [0, y91i[i], y92i[i]]
    line30.set_data(thisjq, thisjjq)

    thiskq = [0, x111j[i], x112j[i]]
    thiskkq = [0, y111j[i], y112j[i]]
    line31.set_data(thiskq, thiskkq)

    thislq = [0, x121k[i], x122k[i]]
    thisllq = [0, y121k[i], y122k[i]]
    line32.set_data(thislq, thisllq)

    thismq = [0, x131l[i], x132l[i]]
    thismmq = [0, y131l[i], y132l[i]]
    line33.set_data(thismq, thismmq)

    thisnq = [0, x141m[i], x142m[i]]
    thisnnq = [0, y141m[i], y142m[i]]
    line34.set_data(thisnq, thisnnq)

    thisoq = [0, x151n[i], x152n[i]]
    thisooq = [0, y151n[i], y152n[i]]
    line35.set_data(thisoq, thisooq)

    thispq = [0, x161o[i], x162o[i]]
    thisppq = [0, y161o[i], y162o[i]]
    line36.set_data(thispq, thisppq)

    thisqa = [0, x171p[i], x172p[i]]
    thisqqa = [0, y171p[i], y172p[i]]
    line37.set_data(thisqa, thisqqa)

    thisrq = [0, x181q[i], x182q[i]]
    thisrrq = [0, y181q[i], y182q[i]]
    line38.set_data(thisrq, thisrrq)

    thissq = [0, x191r[i], x192r[i]]
    thisssq = [0, y191r[i], y192r[i]]
    line39.set_data(thissq, thisssq)

    thistq = [0, x201s[i], x202s[i]]
    thisttq = [0, y201s[i], y202s[i]]
    line40.set_data(thistq, thisttq)

    thisxs = [0, x1List[0][i], x2List[0][i]]
    thisys = [0, y1List[0][i], y2List[0][i]]
    line41.set_data(thisxs, thisys)

    thisxs = [0, x1List[1][i], x2List[1][i]]
    thisys = [0, y1List[1][i], y2List[1][i]]
    line42.set_data(thisxs, thisys)

    thisxs = [0, x1List[2][i], x2List[2][i]]
    thisys = [0, y1List[2][i], y2List[2][i]]
    line43.set_data(thisxs, thisys)

    thisxs = [0, x1List[3][i], x2List[3][i]]
    thisys = [0, y1List[3][i], y2List[3][i]]
    line44.set_data(thisxs, thisys)

    thisxs = [0, x1List[4][i], x2List[4][i]]
    thisys = [0, y1List[4][i], y2List[4][i]]
    line45.set_data(thisxs, thisys)

    thisxs = [0, x1List[5][i], x2List[5][i]]
    thisys = [0, y1List[5][i], y2List[5][i]]
    line46.set_data(thisxs, thisys)

    thisxs = [0, x1List[6][i], x2List[6][i]]
    thisys = [0, y1List[6][i], y2List[6][i]]
    line47.set_data(thisxs, thisys)

    thisxs = [0, x1List[7][i], x2List[7][i]]
    thisys = [0, y1List[7][i], y2List[7][i]]
    line48.set_data(thisxs, thisys)

    thisxs = [0, x1List[8][i], x2List[8][i]]
    thisys = [0, y1List[8][i], y2List[8][i]]
    line49.set_data(thisxs, thisys)

    thisxs = [0, x1List[9][i], x2List[9][i]]
    thisys = [0, y1List[9][i], y2List[9][i]]
    line50.set_data(thisxs, thisys)

    thisxs = [0, x1List[10][i], x2List[10][i]]
    thisys = [0, y1List[10][i], y2List[10][i]]
    line51.set_data(thisxs, thisys)

    thisxs = [0, x1List[11][i], x2List[11][i]]
    thisys = [0, y1List[11][i], y2List[11][i]]
    line52.set_data(thisxs, thisys)

    thisxs = [0, x1List[12][i], x2List[12][i]]
    thisys = [0, y1List[12][i], y2List[12][i]]
    line53.set_data(thisxs, thisys)

    thisxs = [0, x1List[13][i], x2List[13][i]]
    thisys = [0, y1List[13][i], y2List[13][i]]
    line54.set_data(thisxs, thisys)

    thisxs = [0, x1List[14][i], x2List[14][i]]
    thisys = [0, y1List[14][i], y2List[14][i]]
    line55.set_data(thisxs, thisys)

    thisxs = [0, x1List[15][i], x2List[15][i]]
    thisys = [0, y1List[15][i], y2List[15][i]]
    line56.set_data(thisxs, thisys)

    thisxs = [0, x1List[16][i], x2List[16][i]]
    thisys = [0, y1List[16][i], y2List[16][i]]
    line57.set_data(thisxs, thisys)

    thisxs = [0, x1List[17][i], x2List[17][i]]
    thisys = [0, y1List[17][i], y2List[17][i]]
    line58.set_data(thisxs, thisys)

    thisxs = [0, x1List[18][i], x2List[18][i]]
    thisys = [0, y1List[18][i], y2List[18][i]]
    line59.set_data(thisxs, thisys)

    thisxs = [0, x1List[19][i], x2List[19][i]]
    thisys = [0, y1List[19][i], y2List[19][i]]
    line60.set_data(thisxs, thisys)

    thisxs = [0, x1List[20][i], x2List[20][i]]
    thisys = [0, y1List[20][i], y2List[20][i]]
    line61.set_data(thisxs, thisys)

    thisxs = [0, x1List[21][i], x2List[21][i]]
    thisys = [0, y1List[21][i], y2List[21][i]]
    line62.set_data(thisxs, thisys)

    thisxs = [0, x1List[22][i], x2List[22][i]]
    thisys = [0, y1List[22][i], y2List[22][i]]
    line63.set_data(thisxs, thisys)

    thisxs = [0, x1List[23][i], x2List[23][i]]
    thisys = [0, y1List[23][i], y2List[23][i]]
    line64.set_data(thisxs, thisys)

    thisxs = [0, x1List[24][i], x2List[24][i]]
    thisys = [0, y1List[24][i], y2List[24][i]]
    line65.set_data(thisxs, thisys)

    thisxs = [0, x1List[25][i], x2List[25][i]]
    thisys = [0, y1List[25][i], y2List[25][i]]
    line66.set_data(thisxs, thisys)

    thisxs = [0, x1List[26][i], x2List[26][i]]
    thisys = [0, y1List[26][i], y2List[26][i]]
    line67.set_data(thisxs, thisys)

    thisxs = [0, x1List[27][i], x2List[27][i]]
    thisys = [0, y1List[27][i], y2List[27][i]]
    line68.set_data(thisxs, thisys)

    thisxs = [0, x1List[28][i], x2List[28][i]]
    thisys = [0, y1List[28][i], y2List[28][i]]
    line69.set_data(thisxs, thisys)

    thisxs = [0, x1List[29][i], x2List[29][i]]
    thisys = [0, y1List[29][i], y2List[29][i]]
    line70.set_data(thisxs, thisys)

    thisxs = [0, x1List[30][i], x2List[30][i]]
    thisys = [0, y1List[30][i], y2List[30][i]]
    line71.set_data(thisxs, thisys)

    thisxs = [0, x1List[31][i], x2List[31][i]]
    thisys = [0, y1List[31][i], y2List[31][i]]
    line72.set_data(thisxs, thisys)

    thisxs = [0, x1List[32][i], x2List[32][i]]
    thisys = [0, y1List[32][i], y2List[32][i]]
    line73.set_data(thisxs, thisys)

    thisxs = [0, x1List[33][i], x2List[33][i]]
    thisys = [0, y1List[33][i], y2List[33][i]]
    line74.set_data(thisxs, thisys)

    thisxs = [0, x1List[34][i], x2List[34][i]]
    thisys = [0, y1List[34][i], y2List[34][i]]
    line75.set_data(thisxs, thisys)

    thisxs = [0, x1List[35][i], x2List[35][i]]
    thisys = [0, y1List[35][i], y2List[35][i]]
    line76.set_data(thisxs, thisys)

    thisxs = [0, x1List[36][i], x2List[36][i]]
    thisys = [0, y1List[36][i], y2List[36][i]]
    line77.set_data(thisxs, thisys)

    thisxs = [0, x1List[37][i], x2List[37][i]]
    thisys = [0, y1List[37][i], y2List[37][i]]
    line78.set_data(thisxs, thisys)

    thisxs = [0, x1List[38][i], x2List[38][i]]
    thisys = [0, y1List[38][i], y2List[38][i]]
    line79.set_data(thisxs, thisys)

    thisxs = [0, x1List[39][i], x2List[39][i]]
    thisys = [0, y1List[39][i], y2List[39][i]]
    line80.set_data(thisxs, thisys)

    thisxs = [0, x1List[40][i], x2List[40][i]]
    thisys = [0, y1List[40][i], y2List[40][i]]
    line81.set_data(thisxs, thisys)

    thisxs = [0, x1List[41][i], x2List[41][i]]
    thisys = [0, y1List[41][i], y2List[41][i]]
    line82.set_data(thisxs, thisys)

    thisxs = [0, x1List[42][i], x2List[42][i]]
    thisys = [0, y1List[42][i], y2List[42][i]]
    line83.set_data(thisxs, thisys)

    thisxs = [0, x1List[43][i], x2List[43][i]]
    thisys = [0, y1List[43][i], y2List[43][i]]
    line84.set_data(thisxs, thisys)

    thisxs = [0, x1List[44][i], x2List[44][i]]
    thisys = [0, y1List[44][i], y2List[44][i]]
    line85.set_data(thisxs, thisys)

    thisxs = [0, x1List[45][i], x2List[45][i]]
    thisys = [0, y1List[45][i], y2List[45][i]]
    line86.set_data(thisxs, thisys)

    thisxs = [0, x1List[46][i], x2List[46][i]]
    thisys = [0, y1List[46][i], y2List[46][i]]
    line87.set_data(thisxs, thisys)

    thisxs = [0, x1List[47][i], x2List[47][i]]
    thisys = [0, y1List[47][i], y2List[47][i]]
    line88.set_data(thisxs, thisys)

    thisxs = [0, x1List[48][i], x2List[48][i]]
    thisys = [0, y1List[48][i], y2List[48][i]]
    line89.set_data(thisxs, thisys)

    thisxs = [0, x1List[49][i], x2List[49][i]]
    thisys = [0, y1List[49][i], y2List[49][i]]
    line90.set_data(thisxs, thisys)

    thisxs = [0, x1List[50][i], x2List[50][i]]
    thisys = [0, y1List[50][i], y2List[50][i]]
    line91.set_data(thisxs, thisys)

    thisxs = [0, x1List[51][i], x2List[51][i]]
    thisys = [0, y1List[51][i], y2List[51][i]]
    line92.set_data(thisxs, thisys)

    thisxs = [0, x1List[52][i], x2List[52][i]]
    thisys = [0, y1List[52][i], y2List[52][i]]
    line93.set_data(thisxs, thisys)

    thisxs = [0, x1List[53][i], x2List[53][i]]
    thisys = [0, y1List[53][i], y2List[53][i]]
    line94.set_data(thisxs, thisys)

    thisxs = [0, x1List[54][i], x2List[54][i]]
    thisys = [0, y1List[54][i], y2List[54][i]]
    line95.set_data(thisxs, thisys)

    thisxs = [0, x1List[55][i], x2List[55][i]]
    thisys = [0, y1List[55][i], y2List[55][i]]
    line96.set_data(thisxs, thisys)

    thisxs = [0, x1List[56][i], x2List[56][i]]
    thisys = [0, y1List[56][i], y2List[56][i]]
    line97.set_data(thisxs, thisys)

    thisxs = [0, x1List[57][i], x2List[57][i]]
    thisys = [0, y1List[57][i], y2List[57][i]]
    line98.set_data(thisxs, thisys)

    thisxs = [0, x1List[58][i], x2List[58][i]]
    thisys = [0, y1List[58][i], y2List[58][i]]
    line99.set_data(thisxs, thisys)

    thisxs = [0, x1List[59][i], x2List[59][i]]
    thisys = [0, y1List[59][i], y2List[59][i]]
    line100.set_data(thisxs, thisys)

    imin = i
    if imin < 0:
        imin = 0

    time_text.set_text(time_template % (i * dt))

    #return all 100 double pendulums!
    return line, line2, line3, line4, line5, line6, line7, line8, \
           line9, line10, line11, line12, line13, line14, line15, \
           line16, line17, line18, line19, line20, \
           line21, line22, line23, line24, line25, line26, line27, line28, \
           line29, line30, line31, line32, line33, line34, line35, \
           line36, line37, line38, line39, line40, line41, line42, line43,\
           line44, line45, line46, line47, line48, line49, \
           line50, line51, line52, line53, line54, line55, line56, line57, line58, \
           line59, line60, line61, line62, line63, line64, line65, \
           line66, line67, line68, line69, line70, \
           line71, line72, line73, line74, line75, line76, line77, line78, \
           line79, line80, line81, line82, line83, line84, line85, \
           line86, line87, line88, line89, line90, line91, line92, line93, \
           line94, line95, line96, line97, line98, line99, line100, time_text,


#creates and animation object for our simulation
anim = animation.FuncAnimation(fig, animate, np.arange(1, len(b)), interval=30, blit=True, init_func=init)

'''
here is the option to save the simulation as a gif
'''
#f = r"c:\\Users\gusle\Desktop\animation100.gif"
#writergif = animation.PillowWriter(fps=30)
#anim.save(f, writer=writergif)

plt.show() #plays the simulation!