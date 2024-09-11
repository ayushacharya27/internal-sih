from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, db
import serial
import time
import threading
import json
import ml

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate("Add your secret file here")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'add link to your firebase realtime database'
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

                values = [None, None, None, None, None, None, turbidity, ph]
                ecoli = ml.predict(values)
                print(ecoli)

                # Update Firebase
                ref.set({
                    'temperature': temperature,
                    'tds': tds,
                    'turbidity': turbidity,
                    'ph': ph,
                    'ecoli' : ecoli[0]
                }) 

                print(f"Updated Firebase with temp: {temperature}, TDS: {tds}, Turbidity: {turbidity}, pH: {ph}")
            except json.JSONDecodeError as e:
                print(f"Error parsing data: {e}")
            except (KeyError, ValueError) as e:
                print(f"Error extracting values: {e}")

                # 'Dissolved oxygen (DO)', 'Nitrate', 'Orthophosphate', 'Specific conductance', 'Temperature, water', 'Total suspended solids', 'Turbidity', 'pH']

        # time.sleep(5)  # Wait for 5 seconds before the next update

# Start the background thread for serial data reading
thread = threading.Thread(target=read_serial_and_update_firebase)
thread.daemon = True
thread.start()

@app.route('/')
def home():
    return jsonify({"message": "Flask server is running"}), 200

if __name__ == '__main__':
    app.run(debug=True)
