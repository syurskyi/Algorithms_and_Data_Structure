from stay_positive import (tweets, filter_tweets_on_polarity,
                           order_tweets_by_polarity)


def test_filter_tweets_keep_positive():
    actual = filter_tweets_on_polarity(tweets)
    expected = tweets[1:4]
    assert actual == expected


def test_filter_tweets_keep_negative():
    actual = filter_tweets_on_polarity(tweets, keep_positive=False)
    expected = [tweets[0], tweets[-1]]
    assert actual == expected


def test_order_tweets_positive_highest():
    actual = [tweet.polarity for tweet in order_tweets_by_polarity(tweets)]
    expected = [1.0, 0.8, 0.125, -0.19999999999999998,
                -0.3333333333333333]
    assert actual == expected


def test_order_tweets_negative_highest():
    actual = [tweet.polarity for tweet in
              order_tweets_by_polarity(tweets, positive_highest=False)]
    expected = [-0.3333333333333333, -0.19999999999999998,
                0.125, 0.8, 1.0]
    assert actual == expected