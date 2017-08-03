from Extractor import ExtractorBase

extractor = ExtractorBase("#bake")
api = extractor.get_authenticated_handle()
tweets_list = extractor.get_tweets_with_seed_hashtag(api)
extractor.extract_hashtags_per_tweet(tweets_list)
print extractor.rank_hashtags()

