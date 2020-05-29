from flask import Flask, jsonify
from flask_cors import CORS
import tweepy
import json
app= Flask(__name__)

@app.route("/tweets", methods=['GET', 'OPTIONS'])

def hello():
    consumer_key = 'jbrThFMxz7btJnlDFde2wBYya'
    consumer_secret = 'pbLUC48QmqW9V4UinHqv9FcWzkLQsNBPpZLjZuikM9HhyLfnka'
    access_token = '520951268-OYk3LK1LGHvjVinkqyHHN49hxjTLXTZfLYozjXhg'
    access_token_secret = 'GuV7uLyXdxKKXDcuRfuA6oAAJGfFXTR99kMtbJ3gKh2qp'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    cricTweet = tweepy.Cursor(api.search, q='gametimegosser').items(2)
    tweets = {
    'tweetsArr': []
    }
    for tweet in cricTweet:
        tweets['tweetsArr'].append(tweet._json)
        # print(tweet.user.screen_name)
        j = json.dumps(tweets)
        with open('tweets.json', 'w') as f:
            f.write(j)
            f.close()


    op = open('tweets.json')
    data = json.load(op)
    print('test')
   
    return data

if __name__ == '__main__':
    app.run(debug=True)