from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Base, Patient, declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///patient.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/', methods = ['POST', 'GET'])
def Form():
	if request.method == 'POST':
		name = request.form.get('name', 'no name')
		address = request.form.get('address', 'no address')
		email = request.form.get('email', 'no email')
		phone = request.form.get('phone', 'no phone')
		group = request.form.get('group', 'no group')
		policy = request.form.get('policy', 'no policy')

		patient = Patient(name=name,
					address=address)
		session.add(patient)
		session.commit()
		render_template('form.html')
	return render_template('form.html')

if __name__== "__main__":
	app.run(debug=True)