import os
import re
from angrycorner import app

## dotenv
lines = [line.strip() for line in open('.env')]
for line in lines:
  split_line  = line.split("=")
  key         = split_line[0]
  value       = split_line[1]
  os.environ[key] = value

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=True)
