#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib, time, simplejson
from eve import Eve
from pymongo import MongoClient
from flask import request

mongo = MongoClient('api.outpost.travel')
db = mongo.outpost
mongo.admin.authenticate('trevorstarick','Tr1vor8520')
placeRentals = db.placeRentals
accounts = db.accounts

app = Eve()
#app = Eve()

port = 8000
host = '0.0.0.0'

@app.route('/token')
def tokenGen():
	username = request.args.get('username')
	email = request.args.get('email')
	
	timestamp = str(int(time.time()))
	seed = hashlib.md5(username+email+'Ardvark').hexdigest()
	token = hashlib.sha1(username+email+timestamp+seed).hexdigest()
	try:
		accounts.save({'username':username,'email':email,'timestamp':int(timestamp),'token':token,'ip':request.remote_addr})
	except Exception, err:
		if str(err)[:6] == 'E11000':
			return '{"error":"username or email already in use"}'
		else:
			return str(err)
	return '{"token":"'+token+'"}'

@app.route('/count')
@app.route('/count/')
def count():
	a = {}
	for x in placeRentals.distinct('provider'):
		a[x] = placeRentals.find({'provider':x},{'_id':1}).count()
	a['sum'] = placeRentals.count()
	a['unique_cities'] = len(db.placeRentals.distinct('city'))
	return simplejson.dumps(a)

@app.route('/count/sum')
def countSum():
	a = {}
	a['sum'] = placeRentals.count()
	return simplejson.dumps(a)

@app.route('/count/<param>')
def countSingle(param):
	a = {}
	a[param] = placeRentals.find({'provider':param},{'_id':1}).count()
	return simplejson.dumps(a)

if __name__ == '__main__':
	app.run(host=host, port=port, debug=True)