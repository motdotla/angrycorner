# angrycorner

<http://angrycorner.herokuapp.com>

## Usage

```
git clone https://github.com/scottmotte/angrycorner.git
cd angrycorner
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Deploy

```
git clone https://github.com/scottmotte/angrycorner.git
cd angrycorner
heroku addons:add mongohq:small
```

## Documentation

### /

```
curl -X GET http://localhost:5000
```

### /api/trends?lat=[lat]&long=[long]

```
curl -X GET http://localhost:5000/api/trends?lat=[lat]&long=[long]
```

### /api/trends/closest?lat=[lat]&long=[long]

```
curl -X GET http://localhost:5000/api/trends/closest?lat=36.1667&long=-86.7878
```

### /api/trends/place?id=[id]

```
curl -X GET http://localhost:5000/api/trends/place?id=2457170
```

### /api/search?q=[q]

```
curl -X GET http://localhost:5000/api/search?q=%22Bill+Murray%22
```

### /api/magic?lat=[lat]&long=[long]

```
curl -X GET http://localhost:5000/api/magic?lat=36.1667&long=-86.7878
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

## To run the Angry Engine
From the angry engine subdirectory
```
gunicorn main:app
```



type in location. get coordinates back. 

then, a button for 'what should I be angry about'.

Something like that.


Hit twitter for that location and get trends. 

Then hit: 180 per 15 minutes.

trends/locations - hit twitter API.

search on the trends - and get sets of tweets for that trend. Probably returns 20 by default, but we might be able to get more.

We take each of those tweets and then hit our algorithm, then that will give us a %percentage back like 60/40 pos/neg. Then determine based of those 20 - which way are we leaning. 

If we get an angry one, great, then hit it again. 



- super easy to know what to be angry about
- type in location, and bam, like magic
- how we do this? 
- machine learning and firehose
- why
- general public - perspective
- businesses - so good we can filter out your bad tweets
- money from the rich, perspective to the poor
- patent pending anger influence score




# PITCH TO GIVE:

Angry Corner. Angry corner makes it super easy for you to know what to be angry about!

Type in your location, and bam - we deliver something specific to that area and that point in time to be angry about. It's like magic. 

How do we do this? We do this using advanced machine learning on a firehose of tweets.

Why do we do this? 
1) for the general public it's always free. We do this to give you perspective in your life?
2) For businesses, our algorithm is so good that we can filter out any bad tweets about your product. Feel safe and secure at night knowing that you can put a customized feed of your tweets about your company on the homepage of your site without worry of a bad one showing up. And that's how we make money.

We take money from the rich and give perspective to the poor.


We're also considering a patent pending anger influence score - like a twisted Klout score - so you can confirm exactly what you always believed about your angry friends. Shame them with their anger score into tweeting less angry posts.





- we should send a digest email daily of any angry tweets at the company
- we need to reconcile the angry part and the good we are trying to do
- 











## Additional Notes

The #1 thing you should be angry about at this exact minute. Will there be links to things that you should be angry about?

How are you determining what is angry in a city?

Integration w/ traffic data.

How, are you generating revenue? Taking this to different outlets to news or media - to let them gauge the level of anger at a particular location.

What is our unfair advantage - no one does this right now.

How are we going to be the only ones? - By doing it.

Introducing to those people that love being angry. We will introduce it to trolls.

Have you considered any anger influence score - but for mad people. Something for a cloud of anger. A hatred cloud.



## More Notes

Ask questions

"Piss your day off"

Firehose of data

Super advanced algorithms

Eliminate Bad tweets

Patend Pending - Perverted Cloud score for friends

HIVEMIND

Share angry tweets with client.

### Verticals

API access for ad companies - so they can adjust their advertising at a particular time when people are angry in a time and space.

API access for companies to only show good tweets on their website. We'll filter out the bad ones - little js plugin, and we'll email you the bad ones as a digest email that day.




Business plan
Create - what you're making
Distribute - 
Capture - transaction and pricing strategy






How has the model changed over that period. We added google ads - which wasn't originally there. 

Automatic twitter-feed sensor. What's the likelihood that, that happens.

Filter out angry tweets for small businesses? The last one sounds more like a business. Pick the constant theme - this is how we expand into additional markets and put that label on there.

Are you trying to create a business out of this? Absolutely. It's a cool - it's a little contrarian. It hasn't really been done there. Find some sarcastic angry stuff comparisons. 

There are people who always want to complain about something - just want to start a conversation and share some shared anger. You forge a relationship over anger. 

We can convey it a little more strongly if we choose the target a little more specifically. 

Small business - that part is convoluted. 

It would be a good icebreaker for startups. "I definitely think it is something that is just cool"

You are going to let companies understand consumer sentiment - to get them to a purchasing decision.

People will act on emotion like anger - even more than positive anger.

What's that piece of information that if john had, he's gonna buy my product. That's where there is some value for him to speculate on.

Customer's are more likely to share negative emotion. Converting negative emotion to decision making. 







"from good thievery comes good policing" - saying in India

understanding anger to use the knowledge 



Organize the world's emotions (beginning with Anger) and make it universally accessible and useful.


Emotional Intelligence - another vertical for hiring.




## IdeaFrameApp

1. Product or Service:
Angry corner is a way to read the hive mind on the go. Social media has a massive influence on society, and consuming it in a simple way is a problem, we are solving. 

2. Customer:
Casual users who utilize our service in a social manner. 
Businesses or corporations who want to utilize an arbitrage of emotion to better there product.

3. Distribution Methods:
Web service/mobile app

4. Customer Intimacy:
Consumer: Addiction of always being in the know on the hive mind. 
Businesses provides a valuable service for those trying to mine the hivemind for the sentiment of a product.

5. Revenue: 
Charged access to our API so businesses can monitor products. 
Measure of emotional intelligence on individuals. Klout score for emotional intelligence. 

6. Critical Resources:
Machine learning algorithm
User-Experience

7. Partners:
Data partners - unfettered access to firehose data (GNIP, Twitter)

8. Essential Recipe:
Code and build algorithm. Continually improve algorithm. Utilization of mechanical turk for validation.

9. Expenses
Servers
Paid access to data sources
Elance




Emotions. They're all around us and they influence us more than logic. But marketers and businesses have a tough time measuring and tapping into those emotions on a mass scale - the strongest of which is anger.

We're angry corner. We've built a service that makes it easy to read this hivemind of anger on the go.

<<<>>>>>

It's kinda like a perverted Klout score.

Open up the up, click make me angry, and we tell you in time and space what people are angry about. It's that easy using our smart algorithms and advanced machine learning.

Arbitraging emotion for the ALMIGHTY DOLLA'!











## Pitch

State the problem, 
State the solution,
Describe the biz model
- create
- distribute
- capture value

Follow us on twitter at @TheAngryCorner.


* EQ Score - like a perverted klout score
* 3X more likely to share negative experiences
* convert negative sentiment to DOLLA DOLLA BILLS
* hivemind
* arbitraging emotion for the ALMIGHTY DOLLA
* from good thievery comes good policing
* 

====================

We're Angry Corner.

Emotion Intelligence is all around us. It's the new IQ. But it's really hard for businesses to measure on a hivemind and individual level. What if we could change that.

We're angry corner, and we're organizing the world's emotions, beginning with anger. We're making anger universally accessible and useful. 

We've created an algorithm using advanced machine learning to deduce 

====================

Emotions. They're all around us and they influence us more than logic. But marketers and businesses have a tough time measuring and tapping into those emotions on a mass scale - the strongest of which is anger.

We're angry corner. We've built a service that makes it easy to read this hivemind of anger on the go.

<<<>>>>>

It's kinda like a perverted Klout score.

Open up the up, click make me angry, and we tell you in time and space what people are angry about. It's that easy using our smart algorithms and advanced machine learning.

Arbitraging emotion for the ALMIGHTY DOLLA'!








digitizing emotion

harnessing anger for social change

anger makes you stronger, young skywalker

- 3X more likely to share negative experiences
- We can convert negative sentiment to 
- From good thievery comes good policing
- Converting negative emotion to decision making - making you money
- hivemind
- start w/ something negative to grab the people's attention

Angry Corner. Angry corner makes it super easy for you to know what to be angry about!

Type in your location, and bam - we deliver something specific to that area and that point in time to be angry about. It's like magic. 

How do we do this? We do this using advanced machine learning on a firehose of tweets.

Why do we do this? 
1) for the general public it's always free. We do this to give you perspective in your life?
2) For businesses, our algorithm is so good that we can filter out any bad tweets about your product. Feel safe and secure at night knowing that you can put a customized feed of your tweets about your company on the homepage of your site without worry of a bad one showing up. And that's how we make money.

We take money from the rich and give perspective to the poor.


We're also considering a patent pending anger influence score - like a twisted Klout score - so you can confirm exactly what you always believed about your angry friends. Shame them with their anger score into tweeting less angry posts.



Organize the world's emotions (beginning with Anger) and make it universally accessible and useful.




## Takeaways

- 3X more likely to share negative experiences
- We can convert negative sentiment to 
- From good thievery comes good policing
- Converting negative emotion to decision making - making you money
- hivemind
- start w/ something negative to grab the people's attention




1. 
2. 
3. 





## Design inspiration

* finding something angry
* but welcoming at the same time
* secret
* contrarian
* feels like something you want to use because it is so contrarian
* also needs to be simlpe to use. dead easy so you show you friends
* <http://i2.wp.com/boygeniusreport.files.wordpress.com/2014/02/secret-app-iphone.jpg?w=870>
* <http://zagg-blog.s3.amazonaws.com/community/blog/wp-content/uploads/2014/01/secret-app-screenshots-1024x605.jpg>
* [Our twitter](https://twitter.com/theangrycorner)

