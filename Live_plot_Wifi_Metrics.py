import matplotlib.pyplot as plt
import datetime
import time
from IPython.display import display, clear_output

# Initialize the lists to store the Wi-Fi metrics
timestamps = []
rssi_values = []
noise_values = []
tx_rates = []
mcs_indexes = []

# Create subplots
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# Initialize lines for the plots with thinner lines
line1, = ax[0, 0].plot([], [], 'r-', linewidth=0.5)
line2, = ax[0, 1].plot([], [], 'b-', linewidth=0.5)
line3, = ax[1, 0].plot([], [], 'g-', linewidth=0.5)
line4, = ax[1, 1].plot([], [], 'y-', linewidth=0.5)

# Set titles and labels for the subplots
ax[0, 0].set_title('RSSI Value')
ax[0, 0].set_ylabel('RSSI')

ax[0, 1].set_title('Noise Measurement')
ax[0, 1].set_ylabel('Noise')

ax[1, 0].set_title('TX Rate')
ax[1, 0].set_ylabel('TX Rate (Mbps)')

ax[1, 1].set_title('MCS Index')
ax[1, 1].set_ylabel('MCS Index')

# Remove x-axis labels
for axis in ax.flat:
    axis.set_xticks([])
    axis.set_xlabel('')

def update_plot():
    global timestamps, rssi_values, noise_values, tx_rates, mcs_indexes

    # Read the data from the file
    with open('wifi_metrics_output.txt', 'r') as file:
        lines = file.readlines()
        new_data = lines[len(timestamps)+1:]  # Only read new data
        for line in new_data:
            data = line.strip().split(',')
            timestamps.append(datetime.datetime.fromtimestamp(float(data[0])))
            rssi_values.append(int(data[1]))
            noise_values.append(int(data[2]))
            tx_rates.append(float(data[3]))
            mcs_indexes.append(int(data[4]))

    # Keep only the most recent 250 data points
    timestamps = timestamps[-250:]
    rssi_values = rssi_values[-250:]
    noise_values = noise_values[-250:]
    tx_rates = tx_rates[-250:]
    mcs_indexes = mcs_indexes[-250:]

    # Update the data of the plots
    line1.set_data(timestamps, rssi_values)
    ax[0, 0].relim()
    ax[0, 0].autoscale_view()

    line2.set_data(timestamps, noise_values)
    ax[0, 1].relim()
    ax[0, 1].autoscale_view()

    line3.set_data(timestamps, tx_rates)
    ax[1, 0].relim()
    ax[1, 0].autoscale_view()

    line4.set_data(timestamps, mcs_indexes)
    ax[1, 1].relim()
    ax[1, 1].autoscale_view()

while True:
    update_plot()
    clear_output(wait=True)
    display(fig)
    time.sleep(1)
