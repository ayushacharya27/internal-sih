import requests

def send_data_to_server(data, server_url='http://192.168.196.192:5000'):
    """
    Send data to the Flask server.
    
    :param data: List of data to send (e.g., [91398, 7299])
    :param server_url: URL of the Flask server (default is http://172.16.46.77:5000)
    :return: Server response if successful, None otherwise
    """
    try:
        # Send POST request
        response = requests.post(f'{server_url}/ml', json=data)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Print and return the response from the server
        print("Server response:", response.json())
        return response.json()

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    sample_data = [91398, 7299]
    send_data_to_server(sample_data)
    