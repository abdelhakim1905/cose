# Projet COSE (Coordination des Services)

Projet COSE is a service coordination system implemented using Flask, a web framework for Python. The project is designed to demonstrate the coordination of multiple microservices to process and validate user applications for a specific purpose.

## Overview

The system consists of the following microservices:

1. **service_anem:** Accepts user applications, validates the information locally, and coordinates with external services for further validation.

2. **service_etat_civil:** Validates user information such as National Identification Number (NIN), name, surname, and date of birth.

3. **service_cnas_casnos:** Checks the insurance status of an individual based on their NIN.

4. **service_cnr:** Verifies if an individual is a pensioner based on their NIN.

5. **service_notification:** Sends notifications based on the eligibility status of the user's application.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/abdelhakim1905/cose.git

## API Documentation

Explore our API using the interactive Swagger documentation:

[Swagger Documentation](./openapi.json)
