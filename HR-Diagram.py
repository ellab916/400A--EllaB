"""
Created on Wed Sep 4 17:55:43 2024

Author: Ella Butler
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde
import read_mist_models 

df = pd.read_csv("400A Data.csv")
df = df[df["ruwe"]< 1.4] 
df.dropna(subset = ['bp_rp'], inplace = True)
bp_rp = df['bp_rp'] 
mag = df['phot_g_mean_mag']


x_vals = np.nan_to_num(bp_rp)
y_vals = np.nan_to_num(mag)
xy = np.vstack([x_vals, y_vals])


density = gaussian_kde(xy)(xy)

print(density)

plt.scatter(bp_rp, mag, c=density, cmap='plasma')
plt.xlabel("$G_{BP}-G_{RP} (magnitude) $")
plt.ylabel("$M_{G} (magnitude) $")
plt.ylim(21, 6)
plt.colorbar()

isocmd = read_mist_models.ISOCMD('MIST_iso_66e72ace7de02.iso.cmd')


age_ind = isocmd.age_index(7) #returns the index for the desired age
G_mag = isocmd.isocmds[age_ind]['Gaia_G_DR2Rev']
bp = isocmd.isocmds[age_ind]['Gaia_BP_DR2Rev']
rp = isocmd.isocmds[age_ind]['Gaia_RP_DR2Rev']
BP_RP = bp-rp
plt.plot(BP_RP, G_mag) 
plt.ylabel('$M_{G}$')
plt.xlabel('$G_{BP}-G_{RP}$')
plt.xlim(-2, 8)
plt.ylim(21, 6)
print(G_mag)
print(BP_RP)

plt.plot(G_mag, BP_RP, c='blue')

plt.show()

