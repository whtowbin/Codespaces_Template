#%%
import numpy as np 
import pandas as pd

#%%
x = np.arange(1,10)
# %%
def diffuse(x, n):
    for i in range(n):
        x = np.convolve(x, [1, 2, 1], mode='same')
    return x