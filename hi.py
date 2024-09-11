from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, db
import serial
import time
import threading
import json
import requests

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate(r'add path to your secret file here')
firebase_admin.initialize_app(cred, {
    'databaseURL': r'add link to your firebase realtime database'
})

# Reference to the Firebase Realtime Database
ref = db.reference('/sensor')

# Initialize Serial Port
ser = None
try:
    ser = serial.Serial('COM7', 9600)  # Change 'COM3' to your Arduino port
    print("Serial port opened successfully.")
except serial.SerialException as e:
    print(f"Failed to open serial port: {e}")

def send_data_to_server(data, server_url='http://192.168.196.192:5000/ml'):
    """
    Send data to the Flask server.
    
    :param data: List of data to send (e.g., [temperature, tds, turbidity, ph])
    :param server_url: URL of the Flask server (default is http://192.168.196.192:5000/ml)
    :return: Server response if successful, None otherwise
    """
    try:
        # Send POST request
        response = requests.post(server_url, json=data)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Print and return the response from the server
        print("Server response:", response.json())
        return response.json()

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Function to continuously read serial data and update Firebase
def read_serial_and_update_firebase():
    while True:
        if ser and ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"Received data: {line}")

            try:
                # Parse the JSON-like string
                data = json.loads(line)
                temperature = data.get('temperature')
                tds = data.get('tds')
                turbidity = data.get('turbidity')
                ph = data.get('ph')

                # Update Firebase
                ref.child('temperature').set(temperature)
                ref.child('tds').set(tds)
                ref.child('turbidity').set(turbidity)
                ref.child('ph').set(ph)

                # Send data to the server
                send_data_to_server([temperature, tds, turbidity, ph])

                print(f"Updated Firebase with temp: {temperature}, TDS: {tds}, Turbidity: {turbidity}, pH: {ph}")
            except json.JSONDecodeError as e:
                print(f"Error parsing data: {e}")
            except (KeyError, ValueError) as e:
                print(f"Error extracting values: {e}")
        time.sleep(5)  # Wait for 5 seconds before the next update

# Start the background thread for serial data reading
thread = threading.Thread(target=read_serial_and_update_firebase)
thread.daemon = True
thread.start()

@app.route('/')
def home():
    return jsonify({"message": "Flask server is running"}), 200

if __name__ == '__main__':
    app.run(debug=True)
