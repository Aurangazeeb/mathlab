import numpy as np
from mathlab.mathutils import operators as ops

def taylor_series(nterms, indep_var, basefunc, x_val, origin = 0):
	'''
	Makes taylor series upto nterms for basefunc, with starting point
	at origin and evalutates the basefunc wrt to x_val and indep_var
	as sympy Symbol
	
	'''
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
    denom = ops.factorial(i)
    taylor_terms.append((func_at_origin * var_terms)/denom)
  return taylor_terms

def taylor_val(series, indep_var, min = -30, max = 30, precision = 3):
  taylor_func = sum(series)
  taylor_vals = [taylor_func.evalf(n = precision, subs = {indep_var : val}) for val in np.arange(min, max +1)]
  return taylor_vals