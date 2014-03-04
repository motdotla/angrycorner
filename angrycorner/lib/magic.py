import os
import json
from angrycorner import app, db
from bson.objectid import ObjectId
import angrycorner.lib.twitter_api as twitter_api

class Magic():

  def __init__(self, location_uid):
    self.location_uid   = location_uid
    twitter_api_key     = os.environ.get('TWITTER_API_KEY')
    twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
    self.twitter        = twitter_api.Api(twitter_api_key, twitter_api_secret)
 
  def _getDocument(self):
    document = db.locations.find_one({'_id': ObjectId(oid=str(self.location_uid))})
    return document

  def _getTrendsClosestWoeid(self, latitude, longitude):
    result    = self.twitter.get_trends_closest(latitude, longitude)
    
    return result[0]['woeid']

  def _getTrendsPlaceFirstQuery(self, woeid):
    result    = self.twitter.get_trends_place(woeid)

    return result[0]['trends'][0]['query']

  def process(self):
    document  = self._getDocument()

    latitude  = document['lat']
    longitude = document['long']

    woeid     = self._getTrendsClosestWoeid(latitude, longitude)
    query     = self._getTrendsPlaceFirstQuery(woeid)

    result    = self.twitter.get_search(query)
    data      = json.dumps(result)

    return data
