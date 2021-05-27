import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import pandas as pd
import sys
import time

plt.rcParams['figure.figsize'] = 20, 8

#df = pd.read_csv("day.csv")
# df = pd.read_csv("CSV_files/20200608_HFLF.csv")
df = pd.read_csv("test.csv")
#df_picked = df.loc[:, ["cnt"]]
# df_picked = df.loc[:, ["LF/HF"]]
df_picked = df.loc[:, ['x', 'y', 'z']]

df_abnor_check = pd.read_csv("abnormal_cnt_byR.csv")
df_abnor_check = df_abnor_check.iloc[:, 1]

w = 48
m = 2
k = 10
L = 16
Tt = len(df_picked)

abnor_score = np.zeros(Tt)

print(df_picked.head())
print(Tt)
program_start = time.time()
def embed(df, size):
    window = pd.DataFrame()
    window=window.reset_index()
    for i in range(0, len(df)-size+1):
        tmp = df.iloc[i:i+size]
        tep = tmp.dropna()
        tmp = tmp.reset_index()
        window = pd.concat([window, tmp], axis=1)
    window = window.drop(columns="index")
    # window.to_csv("CSV_files/window.csv", index=False)

    return window

for t in range(w+k, Tt-L+1):
    tstart = t-w-k+1
    tend = t
    X1 = pd.DataFrame(embed(df_picked.iloc[tstart:tend, -1], w))
    X1 = X1.iloc[::-1]

    tstart = tstart + L
    tend = tend + L
    X2 = pd.DataFrame(embed(df_picked.iloc[tstart:tend, -1], w))
    X2 = X2.iloc[::-1]

    U1, s1, V1 = np.linalg.svd(X1.astype(np.float64), full_matrices=False)
    U1 = U1[:, 0:m]
    U2, s2, V2 = np.linalg.svd(X2.astype(np.float64), full_matrices=False)
    U2 = U2[:, 0:m]

    U3, s3, V3 = np.linalg.svd(np.dot(U1.T, U2))

    sig1 = s3[0]
    abnor_score[t] = 1 - (sig1 * sig1)

print(t)
# print("...X1...")
# print(X1.head())
# print("...X2...")
# print(X2.head())
# X1.to_csv("CSV_files/X1.csv")
# X2.to_csv("CSV_files/X2.csv")
abnor_score_df = pd.DataFrame(abnor_score, columns=['abnormal'])
data_and_abnor = pd.concat([df.loc[:, ["x", "y", 'z']], abnor_score_df, df_abnor_check], axis=1)

t = df["ts"].astype(np.float64)
fig, ax1 = plt.subplots()
ax1.set_xlabel('DAY(From January 1st, 2011 to December 31st, 2012)')
ax1.set_ylabel("COUNT")
ax1.plot(t, df_picked["x", "y", "z"].astype(np.float64), color='#377ed8', label="LF/HF")
ax2 = ax1.twinx()
ax2.set_ylabel("abnormality")
ax2.plot(abnor_score_df.values, color='#ff7f00', label="abnormal_mashi")
ax2.plot(df_abnor_check.values, color='g', label="abnormal_yuto")

data_and_abnor.to_csv("CSV_files_variation/abnormalscore_rental_bike_day_check.csv", index=False)
plt.grid(True)
plt.legend(loc='upper right')
plt.savefig("PNG_files_variation/abnormalscore_rental_bike_day_check.png")
program_finish = time.time()

elapsed_time = program_finish - program_start
print(f"Execution time:{elapsed_time}sec")