from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # SQLite for simplicity
db = SQLAlchemy(app)

# Define your model (User in this case)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nin = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(20), nullable=False)

@app.route('/inscription', methods=['POST'])
def inscription_service():
    data = request.get_json()

    with app.app_context():
        new_user = User(nin=data['nin'], name=data['name'], dob=data['dob'])

        db.session.add(new_user)
        db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 200

@app.route('/validation/<nin>', methods=['GET'])
def validation_service(nin):
    with app.app_context():
        user = User.query.filter_by(nin=nin).first()

    if user:
        return jsonify({'message': 'Information validated successfully'}), 200
    else:
        return jsonify({'message': 'Invalid information'}), 400

@app.route('/notification/<result>', methods=['GET'])
def notification_service(result):
    if result == 'correct':
        return jsonify({'message': 'You are eligible'})
    elif result == 'incorrect':
        return jsonify({'message': 'You are not eligible'})
    else:
        return jsonify({'message': 'Invalid result'}), 400
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
