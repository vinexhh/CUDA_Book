# -*- coding: utf-8 -*-
"""animations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vcj1jF5tdkNESK91-3o5UK7NNQc2C2JR

Standard imports.
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc

fig, ax = plt.subplots()
plt.close()

ax.set_xlim(( 0, 2))
ax.set_ylim((-2, 2))

line, = ax.plot([], [], lw = 2)

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return (line, )

anim = animation.FuncAnimation(fig, animate, frames = 100, interval = 50, blit = True)
anim.save('animationTest.mp4', fps = 30, extra_args=['-vcodec', 'libx264'])

rc('animation', html = 'jshtml')
anim