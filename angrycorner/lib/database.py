import os
import pymongo
from urlparse import urlparse

class Connect(object):

    token_url = "https://api.twitter.com/oauth2/token"

    def __init__(self):
      MONGOHQ_URL = os.environ.get('MONGOHQ_URL')
      conn        = pymongo.Connection(MONGOHQ_URL)
      # Get the database
      self.db     = conn[urlparse(MONGOHQ_URL).path[1:]]
