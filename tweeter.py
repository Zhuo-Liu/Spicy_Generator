import os
import tweepy as tw
import pandas as pd
import json

import numpy as np
from matplotlib import pyplot as plt


consumer_key = 'UuBgcBDYmzc5e00bS2zdraCdV'
consumer_secret = 'EN1wK53UhRQ4HiyWcsIu97J1bMHEGqAEOejCHMKXpsrtjt63F3'
access_token = '953894378581340160-xHHBeGPxOUE4OVouful1xwojfoBS4BF'
access_secret = 'yEAasKo8lMK9f5w9EBBEqNvFx4jxp8GesBTO8aUVHRl0C'

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tw.API(auth)


# def search_tweets(the_consumer_key, the_consumer_secret, the_access_token_key,
#                   the_access_token_secret, the_proxy_url):
#     """
#     搜索含有特定“内容”的推文
#     :param the_consumer_key: 已有的consumer_key
#     :param the_consumer_secret: 已有的consumer_secret
#     :param the_access_token_key: 已有的access_token_key
#     :param the_access_token_secret: 已有的access_token_secret
#     :param the_proxy_url: 代理及端口号
#     :return:
#     """
#     api = TwitterAPI(consumer_key=the_consumer_key,
#                      consumer_secret=the_consumer_secret,
#                      access_token_key=the_access_token_key,
#                      access_token_secret=the_access_token_secret,
#                      proxy_url=the_proxy_url)
#     r = TwitterPager(api, 'search/tweets', {'q': 'pizza', 'count': 10})
#     for item in r.get_iterator():
#         if 'text' in item:
#             print item['text']
#         elif 'message' in item and item['code'] == 88:
#             print 'SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message']

if __name__ == "__main__":
    auth = tw.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api = tw.API(auth)

    tweets = api.user_timeline('ABC')
    my_list_of_dicts = []
    for each_json_tweet in tweets:
        my_list_of_dicts.append(each_json_tweet._json)
    with open('tweet_json_Trump.txt', 'w') as file:
        file.write(json.dumps(my_list_of_dicts, indent=4))

    # search_words = "#HongKong" + "-filter:retweets"
    # date_since = "2020-11-10"
    # tweets = tw.Cursor(api.search,q=search_words,lang="en",since=date_since).items(10)
    
    # my_list_of_dicts = []
    # for each_json_tweet in tweets:
    #     my_list_of_dicts.append(each_json_tweet._json)
    
    # with open('tweet_json_HongKong.txt', 'w') as file:
    #     file.write(json.dumps(my_list_of_dicts, indent=4))

    # my_demo_list = []

    # with open('tweet_json_HongKong.txt', encoding='utf-8') as json_file:  
    #     all_data = json.load(json_file)
    #     for each_dictionary in all_data:
    #         tweet_id = each_dictionary['id']
    #         text = each_dictionary['text']
    #         favorite_count = each_dictionary['favorite_count']
    #         retweet_count = each_dictionary['retweet_count']
    #         created_at = each_dictionary['created_at']
    #         my_demo_list.append({'tweet_id': str(tweet_id),
    #                             'text': str(text),
    #                             'favorite_count': int(favorite_count),
    #                             'retweet_count': int(retweet_count),
    #                             'created_at': created_at,
    #                             })
    #         #print(my_demo_list)
    #         tweet_json = pd.DataFrame(my_demo_list, columns = 
    #                                 ['tweet_id', 'text', 
    #                                 'favorite_count', 'retweet_count', 
    #                                 'created_at'])
