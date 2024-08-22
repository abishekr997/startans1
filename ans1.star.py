import numpy as np
import matplotlib.pyplot as plt

# Load data from the files
signal_data_1 = np.loadtxt('/content/Data_1.txt')
signal_data_2 = np.loadtxt('/content/Data_2.txt')

# Function to find maxima and minima
def find_extrema(signal_data):
    maxima_indices = []
    minima_indices = []
    for i in range(1, len(signal_data) - 1):
        if signal_data[i] > signal_data[i - 1] and signal_data[i] > signal_data[i + 1]:
            maxima_indices.append(i)
        if signal_data[i] < signal_data[i - 1] and signal_data[i] < signal_data[i + 1]:
            minima_indices.append(i)
    return maxima_indices, minima_indices

# Find maxima and minima for both datasets
maxima_indices_1, minima_indices_1 = find_extrema(signal_data_1)
maxima_indices_2, minima_indices_2 = find_extrema(signal_data_2)

# Plotting the results
def plot_signal(signal_data, maxima_indices, minima_indices, title):
    maxima_indices = np.array(maxima_indices)  # Convert to array for indexing
    minima_indices = np.array(minima_indices)  # Convert to array for indexing

    plt.plot(signal_data, label='Signal')
    plt.scatter(maxima_indices, signal_data[maxima_indices], color='red', label='Maxima')
    plt.scatter(minima_indices, signal_data[minima_indices], color='blue', label='Minima')
    plt.xlabel('Index')
    plt.ylabel('Signal Value')
    plt.title(title)
    plt.legend()
    plt.show()

plot_signal(signal_data_1, maxima_indices_1, minima_indices_1, 'Signal Data Set 1')
plot_signal(signal_data_2, maxima_indices_2, minima_indices_2, 'Signal Data Set 2')

# Printing the indices of the peaks
print("Maxima indices for Signal Data Set 1:", maxima_indices_1)
print("Minima indices for Signal Data Set 1:", minima_indices_1)
print("Maxima indices for Signal Data Set 2:", maxima_indices_2)
print("Minima indices for Signal Data Set 2:", minima_indices_2)
