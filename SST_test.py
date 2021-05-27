import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib import math
import scipy as sp
import pandas as pd
import sys
import time
from fastsst import SingularSpectrumTransformation


sst = SingularSpectrumTransformation(win_length=30)

df = pd.read_csv("polar test.csv")
df2 = pd.read_csv("test.csv")

df_picked = df.loc[:, ['HR (bpm)']]
df_test = df2[df2['sensor_id'] == '810DA3B9']

df_test_x = df_test['x'].reset_index(drop=True, inplace=True)
df_test_y = df_test['y'].reset_index(drop=True, inplace=True)
df_test_z = df_test['z'].reset_index(drop=True, inplace=True)


    
for i in range(0, len(df_test_x)):
    temp = (math.sqrt(abs(df_test_x[i])^2 + abs(df_test_y[i])^2 + abs(df_test_z[i])^2))
    #df_test_norm = pd.Series(temp)
    #print(df_test_x[i], df_test_y[i], df_test_x[i])

#df_test_norm = np.array(df_test_norm)
#df_test_norm.T


score = sst.score_offline(df_picked['HR (bpm)'].values)
#score2 = sst.score_offline(df_test_norm)

print(score)

fig = plt.figure()

plt.plot(score, label="HR")
plt.legend()
#plt.show()

fig.savefig("test_polar.png")