import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///patient.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Patient(Base):
	__tablename__ = 'patient'
	id = Column(Integer, primary_key=True)
	name = Column(UnicodeText(64), nullable=False)
	address = Column(UnicodeText(64))
	email = Column(UnicodeText(64))
	phone = Column(UnicodeText(64))
	group = Column(UnicodeText(64))
	policy = Column(UnicodeText(64))

	@property 
	def serialize(self):
		return {
			'name': self.name,
			'address': self.address,
			'email': self.email,
			'phone': self.phone,
			'group': self.group,
			'policy': self.policy
		} 

Base.metadata.create_all(engine)