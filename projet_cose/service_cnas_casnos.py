from flask import Flask, request, jsonify

app = Flask(__name__)


cnas_casnos_database = [
    {'NIN': '123456789012345', 'insured': True},
    {'NIN': '234567890123456', 'insured': False},
    {'NIN': '345678901234567', 'insured': True},
    {'NIN': '456789012345678', 'insured': True},
    {'NIN': '567890123456789', 'insured': False},
    
]

@app.route('/check_insurance', methods=['POST'])
def check_insurance():
    data = request.get_json()

    # Check if the NIN is in the preloaded database and insured
    if next((item for item in cnas_casnos_database if item['NIN'] == data['NIN'] and item['insured']), None):
        return jsonify({'status': 'insured'})
    else:
        return jsonify({'status': 'not insured'})

if __name__ == '__main__':
    app.run(port=5002)