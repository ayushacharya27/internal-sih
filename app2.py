import serial
import time
from collections import defaultdict

import streamlit as st
import time

# Configure the serial port (adjust as necessary)
 = 'COM15'  # Replace with your serial port
baud_rate = 115200            # Replace with your baud rate
timeout = 0.001                   # Timeout for serial read in seconds

# Create a dictionary to store MAC addresses with their last seen timestamp
mac_addresses = defaultdict(float)

# Time window for active MAC addresses in seconds
time_window = 40

# Initialize the serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=timeout)

def cleanup_old_mac_addresses(current_time):
    """Remove MAC addresses not seen in the last 'time_window' seconds."""
    to_delete = [mac for mac, last_seen in mac_addresses.items() if current_time - last_seen > time_window]
    for mac in to_delete:
        del mac_addresses[mac]
serial_port
def count_active_mac_addresses():
    """Count how many MAC addresses have been active in the last 'time_window' seconds."""
    current_time = time.time()
    cleanup_old_mac_addresses(current_time)
    return len(mac_addresses)


st.title("Real-time Data Display")
st.subheader("Active MAC Addresses in Last 40 Seconds")

placeholder = st.empty()


try:
    print("Monitoring serial data...")
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line:  # Ensure the line is not empty
                mac_address = line
                mac_addresses[mac_address] = time.time()  # Update the timestamp of the MAC address
                active_count = count_active_mac_addresses()
                # print(f"MAC Address: {mac_address} | Active Count (last 40s): {active_count}")
                print(mac_address)

                # placeholder.text(f"Count: {active_count}")
                # st.metric(label="Current Value", value=active_count)
                placeholder.markdown(f"<h3 style='text-align: center; font-size: 72px;'>{active_count}</h3>", unsafe_allow_html=True)

                # address_placeholder.markdown(
                #     f"<h2 style='text-align: center;'>Last 20 Addresses:</h2>"
                #     f"<p style='text-align: center; font-size:18px;'>{'<br>'.join(addresses)}</p>",
                #     unsafe_allow_html=True
                # )
        
        time.sleep(0.001)  # Adjust the sleep time as necessary to control how often the loop runs

except KeyboardInterrupt:
    print("Monitoring stopped.")

finally:
    ser.close()





# Simulate real-time updating of the integer value
# while True:
#     placeholder.text(f"Count: {active_count}")
#     time.sleep(1)