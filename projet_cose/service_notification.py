from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    

    
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5004)
