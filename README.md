# angrycorner

<http://angrycorner.herokuapp.com>

## Usage

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Documentation

### /

```
curl -X GET http://localhost:5000
```

### /trends?lat=[lat]&long=[long]

```
curl -X GET http://localhost:5000/trends?lat=[lat]&long=[long]
```

### /trends/closest?lat=[lat]&long=[long]

```
curl -X GET http://localhost:5000/trends/closest?lat=36.1667&long=-86.7878
```

### /trends/place?id=[id]

```
curl -X GET http://localhost:5000/trends/place?id=2457170
```

## Other

```
pip install git+git://github.com/pedroburon/dotenv.git@master
```

```
pip freeze > requirements.txt
```

```
api = twitter_api.Api(consumer_key, consumer_secret)
```

