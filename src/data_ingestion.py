import pandas as pd
import numpy as np
import os

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/refs/heads/master/Ecommerce%20Customers.csv')

# If you want to keep only columns from the 4th onward, assign it back to df:
df = df.iloc[:, 3:]

df = df[df['Length of Membership']>3]

df.to_csv(os.path.join('data','customer.csv'))