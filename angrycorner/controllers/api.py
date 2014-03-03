import os
import json
import urlparse
from angrycorner import app
from flask import abort, request, make_response
import angrycorner.lib.twitter_api as twitter_api

@app.route('/api/magic')
def magic():

  """ magic """
  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  latitude  = request.args.get('lat', '36.1667')
  longitude = request.args.get('long', '-86.7878')

  result    = api.get_trends_closest(latitude, longitude)
  woeid     = result[0]['woeid']

  result    = api.get_trends_place(woeid)
  query     = result[0]['trends'][0]['query']

  result    = api.get_search(query)
  data      = json.dumps(result)

  r           = make_response( data ) 
  r.mimetype  = 'application/json'

  return r

@app.route('/api/search')
def search():

  """ search """
  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  q = request.args.get('q', '')

  result    = api.get_search(q)

  return json.dumps(result)

@app.route('/api/trends')
def trends():

  """ trends """
  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  latitude  = request.args.get('lat', '36.1667')
  longitude = request.args.get('long', '-86.7878')

  result    = api.get_trends_closest(latitude, longitude)
  woeid     = result[0]['woeid']

  result    = api.get_trends_place(woeid)

  return json.dumps(result)

  
@app.route('/api/trends/closest')
def trends_closest():

  """ trends/closest """

  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  latitude  = request.args.get('lat', '36.1667')
  longitude = request.args.get('long', '-86.7878')

  result = api.get_trends_closest(latitude, longitude)

  return json.dumps(result)

@app.route('/api/trends/place')
def trends_place():

  """ trends/place """

  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  woeid  = request.args.get('id', '2457170')

  result = api.get_trends_place(woeid)

  return json.dumps(result)
