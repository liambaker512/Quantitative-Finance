import numpy as np


# Define the bond cash flows and discount rates:
cash_flows = np.array([-100,10,10,110])
# these are subject for change in input when using the code
discount_rates = np.array([0.05, 0.06, 0.07, 0.08])

# Calculate the present value of each cash flow:
present_values = cash_flows/ ( 1 + discount_rates) ** np.arange(1, len(cash_flows)+1)
#Calculate the bond's price:
price = present_values.sum()

#Calculate the modified duration:
modified_duration = np.dot(np.arange(1,len(cash_flows)+1), present_values)

# Calculate the convexity:
convexity = np.dot(np.arange(1, len(cash_flows)+1) * (np.arange(1, len(cash_flows)+1) + 1), present_values) / price

print("Price:", price)
print("Modified duration:", modified_duration)
print("Convexity:", convexity)