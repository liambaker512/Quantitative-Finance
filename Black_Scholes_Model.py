import math
from scipy.stats import norm

## This is specific for European style options 
# GOAL: Represents the fair value of the option at a given point in time
# This value is relevant because it can be compared to the current market price of the option to determine whether the option is overpriced or underpriced.
## Result : The output of the Black-Scholes model is the theoretical price of an option (Market Value  -  EV = Discount or Premium)
""""
S: the current stock price
K: the strike price of the option
T: the time to maturity of the option (in years)
r: the risk-free interest rate (as a decimal)
sigma: the volatility of the underlying stock (as a decimal)
option_type: either 'call' or 'put', depending on whether you're pricing a call option or a put option
"""

def black_scholes(S, K, T, r, sigma, option_type):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price



##################EXAMPLE#####################
S = 106
K = 125
T = 0.03287671233
r = 0.0483
sigma = 9.9980
option_type = 'put'

price = black_scholes(S, K, T, r, sigma, option_type)
print(price)  # Output: 6.040
