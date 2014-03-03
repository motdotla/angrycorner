import os
from angrycorner import app

## dotenv
lines = [line.strip() for line in open('.env')]
for line in lines:
  split_line  = line.split("=")
  key         = split_line[0]
  value       = split_line[1]
  os.environ[key] = value

print os.environ.get('TWITTER_API_KEY')
print os.environ.get('TWITTER_API_SECRET')

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)
