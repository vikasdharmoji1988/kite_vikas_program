import math
from mpmath import quad
from scipy.stats import norm
from scipy.optimize import brentq

S = 26328.55
K = 26350
T = 2/365     # days -> years
sigma = 0.061 # IV as decimal (6.1% = 0.061)
C_mkt = 65    # call premium

def call_price(r):
    d1 = (math.log(S/K) + r*T + 0.5*sigma**2*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    return S*norm.cdf(d1) - K*math.exp(-r*T)*norm.cdf(d2)

def objective(r):
    return call_price(r) - C_mkt

r=0
value_1=math.log(S/K) 
value_2=.5*sigma**2*T
d_down=sigma*math.sqrt(T)
d1_first_solved=(value_1+value_2)/d_down
d1_first_not_solved= r*T/d_down
sub_straction_value=sigma*math.sqrt(T)
d2_solved=d1_first_solved-sub_straction_value
d2_not_solved=d1_first_not_solved-sub_straction_value


# solve for r between -10% and 20%
r_solution = brentq(objective, -0.10, 0.20)

print("Risk‑free rate =", r_solution)
print("As % =", r_solution*100)
