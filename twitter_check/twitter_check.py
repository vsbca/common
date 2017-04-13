#twitter_check
#It monitors the Twitter for the security threat
#https://media.readthedocs.org/pdf/twittersearch/latest/twittersearch.pdf
#!/usr/bin/python

config = {}
execfile('configuration.py',config)

try:
    from TwitterSearch import *
    import sys
    import codecs
except ImportError:
    print "Please install the rquirement"
    exit()

#creating twitter API object
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

try:
    tso = TwitterSearchOrder()
    tso.set_keywords(['#0day','#exploit','#zero-day','#vulnerability'],or_operator=True)
    tso.set_language('en')

    twitter_stream = TwitterSearch(config["consumer_key"], config["consumer_secret"],config["access_key"], config["access_secret"])


    for tweet in twitter_stream.search_tweets_iterable(tso):
        print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))

except TwitterSearchException as e:
    print e


#credit
#https://dbaumgartel.wordpress.com/2014/03/24/hashtags-in-common-visualizations-with-python-and-twittersearch/
