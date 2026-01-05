import math

def bs_call(S, K, r, T, sigma):
    d1 = (math.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)

    N = lambda x: 0.5*(1 + math.erf(x / math.sqrt(2)))

    return S*N(d1) - K*math.exp(-r*T)*N(d2)


S = 26328.55
K = 26350
T = 2/365
sigma = 0.061   # 6.1% IV as decimal
C_mkt = 65

# --- solve for r by simple iteration ---
r = 0.01   # start guess = 1%
for _ in range(1000):
    price = bs_call(S, K, r, T, sigma)
    diff = C_mkt - price
    if abs(diff) < 1e-6:
        break
    r += diff * 0.1   # small step update

print("Risk‑free rate =", r*100, "%")
