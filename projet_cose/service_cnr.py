from flask import Flask, request, jsonify

app = Flask(__name__)


cnr_database = [
    {'NIN': '123456789012345', 'name': 'Abdelhakim', 'surname': 'Bensaid', 'dob': '1990-03-15'},
    {'NIN': '234567890123456', 'name': 'Safia', 'surname': 'Larbi', 'dob': '1985-07-22'},
    {'NIN': '345678901234567', 'name': 'Karim', 'surname': 'Benmoussa', 'dob': '1992-11-10'},
    {'NIN': '456789012345678', 'name': 'Amina', 'surname': 'Toumi', 'dob': '1988-04-05'},
    {'NIN': '567890123456789', 'name': 'Nadia', 'surname': 'Slimani', 'dob': '1995-09-30'},
    # Add more entries...
]

@app.route('/check_pension', methods=['POST'])
def check_pension():
    data = request.get_json()

    
    # Check if the NIN is in the preloaded database and a pensioner
    if any(item['NIN'] == data['NIN'] for item in cnr_database):
        return jsonify({'status': 'pensioner'})
    else:
        return jsonify({'status': 'not pensioner'})

if __name__ == '__main__':
    app.run(port=5003)