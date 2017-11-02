import tweepy 
from math import log10
from auth import creds
from numpy import mean, arange
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

def hartleyInformation(tweet):
	tweet.strip(' ')
	for w in tweet:
		if w.isalpha() == False:
			tweet.strip(w)
	n = len(tweet)
	s = 26
	H = n * log10(s)
	return H

def meanHartley(list_of_tweets):
	hartleys = []
	for tweet in tweets:
		hartleys.append(hartleyInformation(tweet))

	return mean(hartleys)

if __name__ == '__main__':
	consumer_key, consumer_secret, access_token, access_token_secret = creds()

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth, wait_on_rate_limit=True)

	topics = ["Science", "Meme", "Trump", "Gender", "Politics", "Obama", "Privacy", "Identity", "Security", "Queer", "Hispanic"]
	
	def fetch_tweets():
		tweets_per_topic = []
		for topic in topics:
			tweets = [tweet.text for tweet in api.search(topic)]
			tweets_per_topic.append(tweets)
		return tweets_per_topic

	mean_hartleys = []
	for tweets in fetch_tweets():
		mean_hartleys.append(meanHartley(tweets))

	plt.title('Hartley Information by Topic')
	plt.scatter(arange(len(topics)), mean_hartleys)
	plt.xticks(arange(len(topics)), topics)
	plt.ylabel('Average Hartley Information')

	for topic, x, y in zip(topics, arange(len(topics)), mean_hartleys):
		plt.annotate(topic, xy=(x,y), xytext=(-20,20), textcoords='offset points', ha='right', va='bottom', bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
	
	plt.show()
