from math import log, sqrt, exp
from scipy.stats import norm
from scipy.optimize import brentq

S = 26328.55
K = 26350
r = .0523
T = 2/365
C_mkt = 65

def call_price_bs(sigma):
    if sigma < 1e-12:  # Avoid div by zero
        return max(S - K * exp(-r * T), 0)
    d1 = (log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*sqrt(T))
    d2 = d1 - sigma*sqrt(T)
    return S*norm.cdf(d1) - K*exp(-r*T)*norm.cdf(d2)

def objective(sigma):
    return call_price_bs(sigma) - C_mkt

min_price = call_price_bs(0)
print(f'Min BS price: {min_price:.2f}')
if C_mkt < min_price:
    print('No real IV: market price below min BS price')
else:
    # Find upper bound where objective >0
    upper = 5.0
    while objective(upper) < 0:
        upper *= 2
    iv = brentq(objective, 1e-6, upper)
    print(f'IV: {iv*100:.2f}%')
