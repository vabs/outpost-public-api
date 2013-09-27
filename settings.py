#!/usr/bin/env python
# -*- coding: utf-8 -*-

MONGO_HOST = 'api.outpost.travel'
MONGO_PORT = 27017
MONGO_USERNAME = 'read'
MONGO_PASSWORD = 'outpost123'
MONGO_DBNAME = 'outpost'
SERVER_NAME = 'localhost:8000'
RESOURCE_METHODS = ['GET']
ITEM_METHODS = ['GET']
RATE_LIMIT_GET = 0

DEFAULT_FORMAT = 'json'

placeRentals = {
	'item_title':'place',
	'additional_lookup': {
		'url': '[\w]+',
		'field': 'mid'
	},
	'resource_methods':['GET'],
	'schema':{
		'origin':{
			'type':'string',
		},
		'roomType':{
			'type':'string',
		},
		'hostName':{
			'type':'string',
		},
		'description':{
			'type':'string',
		},
		'logoLV':{
			'type':'string',
		},
		'ratePer':{
			'type':'string',
		},
		'latLng':{
			'type':'list',
		},
		'address':{
			'type':'string',
		},
		'pid':{
			'type':'string',
		},
		'microProvider':{
			'type':'string',
		},
		'currency':{
			'type':'string',
		},
		'rate':{
			'type':'integer',
		},
		'shortLink':{
			'type':'string',
		},
		'occupancy':{
			'type':'integer',
		},
		'responseTime':{
			'type':'string',
		},
		'propertyType':{
			'type':'string',
		},
		'captions':{
			'type':'list',
		},
		'roomTypeAlias':{
			'type':'string',
		},
		'logoSV':{
			'type':'string',
		},
		'logoDesc':{
			'type':'string',
		},
		'propertyTypeAlias':{
			'type':'string',
		},
		'city':{
			'type':'string',
		},
		'houseRules':{
			'type':'string',
		},
		'photos':{
			'type':'list',
		},
		'smallInfo':{
			'type':'list',
		},
		'mid':{
			'type':'string',
			'required':True,
			'unique':True,
		},
		'currencySign':{
			'type':'string',
		},
		'thumbnail':{
			'type':'string',
		},
		'fullProvider':{
			'type':'string',
		},
		'bathroomCount':{
			'type':'integer',
		},
		'amenities':{
			'type':'list',
		},
		'bedCount':{
			'type':'integer',
		},
		'provider':{
			'type':'string',
		},
		'bedroomCount':{
			'type':'integer',
		},
		'heading':{
			'type':'string',
		},
	}
}
experiences = {
	'item_title':'experience',
	'additional_lookup': {
		'url': '[\w]+',
		'field': 'mid'
	},
	'resource_methods':['GET'],
	'schema':{
		'origin':{
			'type':'string',
		},
		'logoLV':{
			'type':'string',
		},
		'hostName':{
			'type':'string',
		},
		'pid':{
			'type':'string',
		},
		'rate':{
			'type':'integer',
		},
		'captions':{
			'type':'list',
		},
		'logoSV':{
			'type':'string',
		},
		'logoDesc':{
			'type':'string',
		},
		'city':{
			'type':'string',
		},
		'hostPhoto':{
			'type':'string',
		},
		'fullProvider':{
			'type':'string',
		},
		'mid':{
			'type':'string',
			'required':True,
			'unique':True,
		},
		'occupancy':{
			'type':'integer',
		},
		'details':{
			'type':'list',
		},
		'provider':{
			'type':'string',
		},
		'thumbnail':{
			'type':'string',
		},
		'description':{
			'type':'string',
		},
		'latLng':{
			'type':'list',
		},
		'ratePer':{
			'type':'string',
		},
		'microProvider':{
			'type':'string',
		},
		'photos':{
			'type':'list',
		},
		'shortLink':{
			'type':'string',
		},
		'address':{
			'type':'string',
		},
		'date':{
			'type':'string',
		},
		'smallInfo':{
			'type':'list',
		},
		'heading':{
			'type':'string',
		},
	}
}
rideShares = {
	'item_title':'rideShare',
	'additional_lookup': {
		'url': '[\w]+',
		'field': 'mid'
	},
	'resource_methods':['GET'],
	'schema':{
		'origin':{
			'type':'string',
		},
		'idtype':{
			'type':'string',
		},
		'lables':{
			'type':'list',
		},
		'seat':{
			'type':'integer',
		},
		'price2':{
			'type':'string',
		},
		'id':{
			'type':'string',
		},
		'full_provider':{
			'type':'string',
		},
		'img':{
			'type':'string',
		},
		'destination':{
			'type':'string',
		},
		'mid':{
			'type':'string',
			'required':True,
			'unique':True,
		},
		'logopath':{
			'type':'string',
		},
		'logodesc':{
			'type':'string',
		},
		'timestamp':{
			'type':'integer',
		},
		'price':{
			'type':'integer',
		},
		'microProvider':{
			'type':'string',
		},
		'shortLink':{
			'type':'string',
		},
		'date':{
			'type':'string',
		},
		'destLatLng':{
			'type':'list',
		},
		'desc':{
			'type':'string',
		},
		'originLatLng':{
			'type':'list',
		},
		'name':{
			'type':'string',
		},
		'age':{
			'type':'string',
		},
		'uri':{
			'type':'string',
		},
		'currencySign':{
			'type':'string',
		},
		'time':{
			'type':'string',
		},
		'heading':{
			'type':'string',
		},
	}
}

DOMAIN = {
	'placeRentals': placeRentals,
	'experiences': experiences,
	'rideShares': rideShares,
}
