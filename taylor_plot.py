import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import sympy as sp
# from mathutils import operators as ops
from mathlab import taylor

x = sp.Symbol('x')
num_pow = 2
y = 5*x**2 + 23*x**5 + 3*x**8


# 2 /(x**num_pow - x)

#5*x**2 + (x**3) - 34*x**-2
#

baseline = [y.evalf(n =3, subs = dict(x = val)) for val in np.arange(-30, 30)]

ref_point = 30
num_terms = 1
taylorseries = taylor.taylor_series(num_terms, x, y, x, ref_point)

taylor_value = taylor.taylor_val(taylorseries, x)
plt.plot(baseline, label = 'baseline', linestyle = '--', lw = 5)
plt.plot(taylor_value, label = 'taylor')

def animate(interval):
  plt.cla()
  global num_terms
  num_terms += 1
  print(f'Approximating to {num_terms} taylor terms')
  taylorseries = taylor.taylor_series(num_terms, x, y, x, ref_point)
  taylor_value = taylor.taylor_val(taylorseries, x)
  plt.plot(baseline, label = 'baseline', linestyle = '--', lw = 5);plt.plot(taylor_value, label = 'taylor')
  #plt.xlim(-10,90); 
  #plt.ylim(-100, 100)
  
  plt.legend(loc = 'upper right')
  #plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()
plt.show()