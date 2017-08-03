import tweepy
import helpers

class ExtractorBase(object):
	def __init__(self, seed_hashtag):
		self.seed_hashtag = seed_hashtag
		self.hashtag_dict = {}

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


	# Extract co-occuring hashtags
	def extract_hashtags_per_tweet(self, tweets_list):
		for tweet in tweets_list:
			tweet_id = tweet.id_str;
			for hashtag in tweet.entities['hashtags']:
				hastagText = hashtag['text'].encode("ascii", "replace").lower()
				self.add_hashtag_to_dict(hastagText, tweet_id)

	def add_hashtag_to_dict(self, hashtag, tweet_id):
		if hashtag in self.hashtag_dict:
			self.hashtag_dict[hashtag].add(tweet_id)
		else:
			self.hashtag_dict[hashtag] = set([tweet_id])


	# Rank co-occuring hashtags
	def rank_hashtags(self):
		return map(lambda sorted_hashtag_tuple: sorted_hashtag_tuple[0], sorted(self.hashtag_dict.items(), key= lambda x: len(x[1]), reverse=True))




