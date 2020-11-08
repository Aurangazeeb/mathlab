import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import sympy as sp


def factorial(n):
  val = 1
  for i in range(1, n+1):
    val *= i
  return val

x = sp.Symbol('x')
num_pow = 2
y = 2 /(x**num_pow - x)

#5*x**2 + (x**3) - 34*x**-2
#

baseline = [y.evalf(n =3, subs = dict(x = val)) for val in np.arange(-30, 30)]


def taylor_series(nterms, indep_var, basefunc, x_val, origin = 0):
  baseval = basefunc.evalf(n =3, subs = {indep_var : origin})
  # print('baseval :', baseval)
  taylor_terms = [baseval]
  for i in range(1, nterms):
    basefunc = basefunc.diff(indep_var)
    # print(dict(basefunc = basefunc))
    func_at_origin = basefunc.evalf(n=3 , subs = {indep_var : origin})
    # yprime_vals = [baseval]
    xoffset =  x_val - origin
    var_terms = xoffset**i
    denom = factorial(i)
    taylor_terms.append((func_at_origin * var_terms)/denom)
  return taylor_terms

def taylor_val(series, min = -30, max = 30, precision = 3):
  taylor_func = sum(series)
  taylor_vals = [taylor_func.evalf(n = precision, subs = {x : val}) for val in np.arange(min, max +1)]
  return taylor_vals

ref_point = 30
num_terms = 1
taylorseries = taylor_series(num_terms, x, y, x, ref_point)

taylor_value = taylor_val(taylorseries)
plt.plot(baseline, label = 'baseline', linestyle = '--', lw = 5)
plt.plot(taylor_value, label = 'taylor')

def animate(interval):
  plt.cla()
  global num_terms
  num_terms += 1
  print(f'Approximating to {num_terms} taylor terms')
  taylorseries = taylor_series(num_terms, x, y, x, ref_point)
  taylor_value = taylor_val(taylorseries)
  plt.plot(baseline, label = 'baseline', linestyle = '--', lw = 5);plt.plot(taylor_value, label = 'taylor')
  #plt.xlim(-10,90); 
  #plt.ylim(-100, 100)
  
  plt.legend(loc = 'upper right')
  #plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()
plt.show()