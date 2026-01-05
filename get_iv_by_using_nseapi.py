import nsefin as nse
import pandas as pd

# Fetch option chain for NIFTY

x=nse.get_nse_instance()
oc_data = x.get_option_chain("NIFTY")
# The returned data frame typically includes an 'Implied Volatility' column
print(oc_data)
