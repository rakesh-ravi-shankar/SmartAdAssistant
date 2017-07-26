import tweepy
import helpers

class ExtractorBase(object):
	def __init__(self, seed_hashtag):
		self.seed_hashtag = seed_hashtag

	# Get the decrypted auth credentials
	def get_auth_credentials(self):
		auth_credentials = helpers.decrypt_file("auth_credentials.json.encoded")
		consumer_key = auth_credentials["consumer_key"]
		consumer_secret = auth_credentials["consumer_secret"]
		access_key = auth_credentials["access_key"]
		access_secret = auth_credentials["access_secret"]
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key, access_secret)
		return auth

	# Create a tweepy api object
	def get_authenticated_handle(self):
		return tweepy.API(self.get_auth_credentials(),
							wait_on_rate_limit=True,
							wait_on_rate_limit_notify=True)


	# Find all tweets with seed hashtag
	def get_tweets_with_seed_hashtag(self, api):
		return api.search(q=self.seed_hashtag, count=100)


	# TODO: Add logic to this template function
	# Extract co-occuring hashtags
	def extract_hashtags_per_tweet(self, tweets_list):
		pass


	# TODO: Add logic to this template function
	# Rank co-occuring hashtags
	def rank_hashtags(self, formatted_tweet):
		pass