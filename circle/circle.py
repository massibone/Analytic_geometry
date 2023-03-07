# x**2  + y**2 = r**2
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-30,30,100)
fig, ax = plt.subplots()

ax.set_aspect('equal')

ax.grid(True, which='both')

ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')



r = 6
x = np.linspace(-r,r,1000)
y = np.sqrt(-x**2+r**2)
plt.plot(x, y,'b')
plt.plot(x,-y,'b')

ax.set(xlim=(-7, 7), ylim=(-7, 7),
       xlabel='y', ylabel='x',
       title='circle')
plt.show()