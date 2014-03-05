import os
import json
from angrycorner import app, db
from bson.objectid import ObjectId
import angrycorner.lib.twitter_api as twitter_api
import angrycorner.lib.angry_engine.classifier.classifier as classifier

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

  def _filterToStatuses(self, query):
    result    = self.twitter.get_search(query)

    statuses  = result['statuses']
    status_texts = []
    for status in statuses:
      status_texts.append(status['text'])

    return status_texts

  def _sentimentizeThatIsh(self, statuses):
    angry_classifier  = classifier.AngryClassifier()
    sentiment         = angry_classifier.classify_tweets(statuses)

    return sentiment
 
  def _normalizeThoseSentiments(self, statuses):
    angry_classifier  = classifier.AngryClassifier()
    sentiment         = angry_classifier.normalize_happy_angry_values_from_tweets(statuses)

    return sentiment

  def process(self):
    document  = self._getDocument()

    latitude  = document['lat']
    longitude = document['long']

    woeid         = self._getTrendsClosestWoeid(latitude, longitude)
    query         = self._getTrendsPlaceFirstQuery(woeid)
    statuses      = self._filterToStatuses(query)
    result        = self._sentimentizeThatIsh(statuses)

    db.locations.update({'_id': ObjectId(oid=str(self.location_uid))}, { "$set": { "processed": True }}, True)

    data = str(result)

    return data

  def process_to_attitudes(self):
    document  = self._getDocument()

    latitude  = document['lat']
    longitude = document['long']

    woeid         = self._getTrendsClosestWoeid(latitude, longitude)
    query         = self._getTrendsPlaceFirstQuery(woeid)
    statuses      = self._filterToStatuses(query)
    result        = self._normalizeThoseSentiments(statuses)

    print result

    db.locations.update({'_id': ObjectId(oid=str(self.location_uid))}, { "$set": { "processed": True }}, True)
    db.locations.update({'_id': ObjectId(oid=str(self.location_uid))}, { "$set": { "weights": result }}, True)

    data = str(result)

    return data

  def a(self, username):
    statuses      = self.twitter.get_timeline(username)

    status_texts  = []
    for status in statuses:
      status_texts.append(status['text'])

    print len(status_texts)
    print status_texts
    result        = self._normalizeThoseSentiments(status_texts)

    return result


