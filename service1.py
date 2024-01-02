from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Local database to store received data
local_database = []

# Second service URL
service2_url = "http://localhost:5001/check_info"

@app.route('/save_info', methods=['POST'])
def save_info():
    data = request.get_json()

    # Save data to local database
    local_database.append(data)

    # Send data to the second service for verification
    response = requests.post(service2_url, json=data)
    
    if response.status_code == 200 and response.json()['status'] == 'found':
        return jsonify({'status': 'granted'})
    else:
        return jsonify({'status': 'not allowed'})

if __name__ == '__main__':
    app.run(port=5000)
