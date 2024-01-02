from flask import Flask, request, jsonify

app = Flask(__name__)


etat_civil_database = [
    {'NIN': '123456789012345', 'name': 'Abdelhakim', 'surname': 'Bensaid', 'dob': '1990-03-15'},
    {'NIN': '234567890123456', 'name': 'Safia', 'surname': 'Larbi', 'dob': '1985-07-22'},
    {'NIN': '345678901234567', 'name': 'Karim', 'surname': 'Benmoussa', 'dob': '1992-11-10'},
    {'NIN': '456789012345678', 'name': 'Amina', 'surname': 'Toumi', 'dob': '1988-04-05'},
    {'NIN': '567890123456789', 'name': 'Nadia', 'surname': 'Slimani', 'dob': '1995-09-30'},
    
]

@app.route('/validate_info', methods=['POST'])
def validate_info():
    data = request.get_json()

    
    if any(entry['NIN'] == data['NIN'] for entry in etat_civil_database):
        return jsonify({'status': 'info validated'})
    else:
        return jsonify({'status': 'info not validated'})

if __name__ == '__main__':
    app.run(port=5001)
