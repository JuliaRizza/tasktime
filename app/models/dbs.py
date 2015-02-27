# -*- coding: utf-8 -*-
from app import db
from werkzeug.security import generate_password_hash

import datetime

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	## user info
	name = db.Column(db.String)
	email = db.Column(db.String)
	passowrd = db.Column(db.String)
	category = db.Column(db.Enum('master', 'employee'),\
		default='employee')
	## company info
	company_name = db.Column(db.String) ## PT-BR: Razão Social
	trade_name = db.Column(db.String) ## PT-BR: Nome Fantasia
	company_federal_id = db.Column(db.String) ## PT-BR: CNPJ
	company_state_id = db.Column(db.String) ## PT-BR: Inscrição Estadual
	## contact info
	address = db.Column(db.String)
	number = db.Column(db.Integer)
	complement = db.Column(db.String(20))
	zip_code = db.Column(db.String)
	city = db.Column(db.String)
	state = db.Column(db.String)
	country = db.Column(db.String)
	phone = db.Column(db.String)
	celphone = db.Column(db.String)

	def __repr__(self):
		return '<User %r>' % self.name

class Client(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	## user info
	name = db.Column(db.String) 
	email = db.Column(db.String)
	password = db.Column(db.String)
	## company info
	company_name = db.Column(db.String) ## PT-BR: Razão Social
	trade_name = db.Column(db.String) ## PT-BR: Nome Fantasia
	company_federal_id = db.Column(db.String) ## PT-BR: CNPJ
	company_state_id = db.Column(db.String) ## PT-BR: Inscrição Estadual
	## contact info
	address = db.Column(db.String)
	number = db.Column(db.Integer)
	complement = db.Column(db.String(20))
	zip_code = db.Column(db.String)
	city = db.Column(db.String)
	state = db.Column(db.String)
	country = db.Column(db.String)
	phone = db.Column(db.String)
	celphone = db.Column(db.String)



	def __repr__(self):
		return '<Client %r - %r>' % (self.name - self.trading_name)

class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	description = db.Column(db.Text)
	clients = db.Column(db.Integer, db.ForeignKey('client.id'))

	def __repr__(self):
		return '<Project %r>' % self.name

class Article(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	content = db.Column(db.String)
	attachments = db.Column(db.String)
	author = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Article %r>' % self.name

class Contract(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	price_hour = db.Column(db.Float)
	total_hours = db.Column(db.Integer, default=1)
	period = db.Column(db.Integer, default=1) #in months
	attachment = db.Column(db.String)

	def __repr__(self):
		return '<Contract %r>' % self.title

class Ticket(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	description = db.Column(db.Text)
	priority = db.Column(db.Enum('high', 'normal', \
		'low'), default='normal')
	status = db.Column(db.Enum('open', 'closed', \
		'on hold'), default='open')
	start_time = db.Column(db.DateTime, default=datetime.datetime.now)
	end_time = db.Column(db.DateTime)
	project = db.Column(db.Integer, db.ForeignKey('project.id'))
	client = db.Column(db.Integer, db.ForeignKey('client.id'))
	employee = db.Column(db.Integer, db.ForeignKey('user.id'))
	contract = db.Column(db.Integer, db.ForeignKey('contract.id'))

	def __repr__(self):
		return '<Ticket %r>' % self.title
    

