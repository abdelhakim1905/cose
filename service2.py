from flask import Flask, request, jsonify

app = Flask(__name__)

# Preloaded database of id numbers and names
preloaded_database = [
    {'id': 1, 'name': 'Person1'},
    {'id': 2, 'name': 'Person2'},
    {'id': 3, 'name': 'Person3'},
    {'id': 4, 'name': 'Person4'},
    {'id': 5, 'name': 'Person5'}
]

@app.route('/check_info', methods=['POST'])
def check_info():
    data = request.get_json()

    # Check if the information is in the preloaded database
    if data in preloaded_database:
        return jsonify({'status': 'found'})
    else:
        return jsonify({'status': 'not found'})

if __name__ == '__main__':
    app.run(port=5001)
