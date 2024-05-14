# RF-Based-Drone-Detection-and-Classification
Developed a Python script to process radio frequency data for drone detection.

Loaded large datasets from CSV files using numpy.

Segmented the data into 1-second intervals (1,000,000 data points at 80 MHz).

Computed the Short-Time Fourier Transform (STFT) of each segment using scipy.signal.stft.

Generated spectrogram images from the STFT results using matplotlib.pyplot.

Saved each spectrogram as a .jpg file, with the file name indicating the time segment.
