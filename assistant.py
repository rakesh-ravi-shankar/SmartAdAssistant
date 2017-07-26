from Extractor import ExtractorBase
import helpers


extractor = ExtractorBase("#bake")
api = extractor.get_authenticated_handle()
tweets_list = extractor.get_tweets_with_seed_hashtag(api)
print tweets_list

# TODO: Find co-occuring hashtags
# TODO: Rank co-occuring hashtags
