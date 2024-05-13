import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import stft

file_folder = 'D:\\project\\DroneRF\\Bepop drone\\RF Data_10000_L\\RF Data_10000_L'
filepath = 'D:\\project\\Bepop_H_L\\low'
Fs = 80e6
N = 1e7

# List of file names
files = ['10000H_' + str(i) + '.csv' for i in range(0, 21)]  # Generates file names from '10000H_2.csv' to '10000H_20.csv'

for file in files:
    data = np.loadtxt(os.path.join(file_folder, file), delimiter=",")
    i = 0
    while(i < N):
        s = data[i:i+1000000]
        frequencies, times, Sxx = stft(s, fs=Fs, nperseg=32)
        name = file.replace('.csv', '') + '_' + str(i//1000000) + '.jpg'
        plt.pcolormesh(times, frequencies, np.abs(Sxx), cmap='plasma')
        plt.axis('off')
        plt.savefig(os.path.join(filepath, name), bbox_inches='tight')
        plt.close()  
        print("File saved:", name)
        i += 1000000