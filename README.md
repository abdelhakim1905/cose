# cose
Projet COSE (Coordination des Services)
Projet COSE is a service coordination system implemented using Flask, a web framework for Python. The project is designed to demonstrate the coordination of multiple microservices to process and validate user applications for a specific purpose.

Overview
The system consists of the following microservices:

service_anem: Accepts user applications, validates the information locally, and coordinates with external services for further validation.

service_etat_civil: Validates user information such as National Identification Number (NIN), name, surname, and date of birth.

service_cnas_casnos: Checks the insurance status of an individual based on their NIN.

service_cnr: Verifies if an individual is a pensioner based on their NIN.

service_notification: Sends notifications based on the eligibility status of the user's application.

Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/projet_cose.git
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the services:

bash
Copy code
cd projet_cose
python service_anem.py
python service_etat_civil.py
python service_cnas_casnos.py
python service_cnr.py
python service_notification.py
Submit an application:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"NIN": "123456789012345", "name": "John", "surname": "Doe", "dob": "1990-01-01"}' http://localhost:5000/submit_application
License
This project is licensed under the MIT License - see the LICENSE file for details.

Please customize this template according to the specifics of your project. You may want to add more details, such as the purpose of the project, instructions for running the services in a Docker container, or any other relevant information.
