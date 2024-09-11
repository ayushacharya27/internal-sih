from flask import Flask, request, jsonify
from collections import deque
from datetime import datetime, timedelta

app = Flask(__name__)

# Use a deque to store the last 100 records (adjust as needed)
data_store = deque(maxlen=100)

@app.route('/ml', methods=['POST'])
def receive_data():
    try:
        # Parse the incoming JSON data
        json_data = request.json
        
        # Ensure the data is a tuple
        if not isinstance(json_data, list):
            return jsonify({"error": "Data must be a tuple (list in JSON)"}), 400
        
        # Store the data along with the current timestamp
        timestamp = datetime.now()
        data_store.append((timestamp, tuple(json_data)))
        print(data_store)
        
        return jsonify({"message": "Data received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/', methods=['GET'])
def get_recent_data():
    try:
        # Get the time interval from query parameters (default to 1 hour)
        hours = float(request.args.get('hours', 1))
        
        # Calculate the cutoff time
        cutoff_time = datetime.now() - timedelta(hours=hours)
        
        # Filter and return the last 20 records within the time interval
        recent_data = [
            {"timestamp": item[0].isoformat(), "data": item[1]}
            for item in list(data_store)[-20:]
            if item[0] >= cutoff_time
        ]
        
        return jsonify(recent_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)