from flask import Flask
import os
import pymongo
from urlparse import urlparse

## dotenv
try:
  current_dir   = os.path.dirname(__file__)
  rel_env_path  = "../.env"
  abs_file_path = os.path.join(current_dir, rel_env_path)
  lines         = [line.strip() for line in open(abs_file_path)]
  for line in lines:
    split_line  = line.split("=")
    key         = split_line[0]
    value       = split_line[1]
    os.environ[key] = value
except:
  pass

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "2091/data.txt"
abs_file_path = os.path.join(script_dir, rel_path)

conn    = pymongo.Connection(os.environ.get('MONGOHQ_URL'))
db      = conn[urlparse(os.environ.get('MONGOHQ_URL')).path[1:]]
app     = Flask(__name__)

from angrycorner.controllers import index, api

