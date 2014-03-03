import os
import json
import urlparse
from angrycorner import app
from flask import abort, request, make_response
import angrycorner.lib.twitter_api as twitter_api

@app.route('/trends/closest')
def trends_closest():

  """ trends/closest """

  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  latitude  = request.args.get('lat', '37.781157')
  longitude = request.args.get('long', '-122.400612831116')

  result = api.get_trends_closest(latitude, longitude)

  return json.dumps(result)
