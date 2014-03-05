import os
import json
import urlparse
from angrycorner import app, db
from bson.objectid import ObjectId
from flask import abort, request, make_response
import angrycorner.lib.twitter_api as twitter_api
import angrycorner.lib.magic as magic

@app.route('/api/location')
def create_location():
  latitude  = request.args.get('lat', '36.1667')
  longitude = request.args.get('long', '-86.7878')

  id = db.locations.insert({"lat":latitude, "long":longitude})

  resp = {
    'success': True,
    'location': {
      'id': str(id),
      'lat': latitude,
      'long': longitude,
      'processed': False
    }
  }

  data        = json.dumps(resp)
  r           = make_response(data)
  r.mimetype  = 'application/json'
  return r

@app.route('/api/location/<id>')
def get_location(id):
  document = db.locations.find_one({'_id': ObjectId(oid=str(id))})

  if document == None:
    r           = make_response('{"success": "false"}')
    r.mimetype  = 'application/json'
    return r
   
  resp = {
    'success': True,
    'location': {
      'id': str(id),
      'lat': document['lat'],
      'long': document['long'],
      'processed': document.get('processed', False),
      'message': "ANGRY MESSAGE HERE"
    }
  }

  data        = json.dumps(resp)
  r           = make_response(data)
  r.mimetype  = 'application/json'

  return r

@app.route('/api/process/<id>')
def process(id):
  magician  = magic.Magic(id)
  data      = magician.process()

  r           = make_response( data ) 
  r.mimetype  = 'application/json'

  return r

@app.route('/api/process_to_attidues/<id>')
def process_to_attitudes(id):
  magician  = magic.Magic(id)
  data      = magician.process_to_attitudes()

  r           = make_response( data ) 
  r.mimetype  = 'application/json'

  return r
