from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


inscription_database = []


etat_civil_url = "http://localhost:5001/validate_info"
cnas_casnos_url = "http://localhost:5002/check_insurance"
cnr_url = "http://localhost:5003/check_pension"
notification_url = "http://localhost:5004/send_notification"

@app.route('/submit_application', methods=['POST'])
def submit_application():
    data = request.get_json()
    
    print("Received data:", data)

    
    inscription_database.append(data)

    
    response_etat_civil = requests.post(etat_civil_url, json=data)
    response_cnas_casnos = requests.post(cnas_casnos_url, json=data)
    response_cnr = requests.post(cnr_url, json=data)
    print("Response from etat_civil:", response_etat_civil.text)
    print("Response from cnas_casnos:", response_cnas_casnos.text)
    print("Response from cnr:", response_cnr.text)
    
    if (
        response_etat_civil.status_code == 200 and response_etat_civil.json()['status'] == 'info validated' and
        response_cnas_casnos.status_code == 200 and response_cnas_casnos.json()['status'] == 'insured' and
        response_cnr.status_code == 200 and response_cnr.json()['status'] == 'pensioner'
    ):
        eligibility_status = 'eligible'
    else:
        eligibility_status = 'not eligible'

    
    #response_notification = requests.post(notification_url, json={'status': eligibility_status, 'user_data': data})

    return jsonify({'status': 'application submitted', 'eligibility_status': eligibility_status})

if __name__ == '__main__':
    app.run(port=5000)
