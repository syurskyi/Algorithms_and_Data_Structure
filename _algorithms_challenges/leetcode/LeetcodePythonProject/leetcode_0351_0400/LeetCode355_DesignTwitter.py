'''
Created on Feb 28, 2018

@author: tongq
'''
class TweetObj(object):
    def __init__(self, tweet_id, user_id, tweetId, prevTweet=None):
        self.user_id = user_id
        self.tweetContext = tweetId
        self.prevTweet = prevTweet
        self.tweet_id = tweet_id

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.following = {}
        self.latestTweets = {}
        self.tweet_id = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.following:
            self.following[userId] = set([userId])
        self.tweet_id += 1
        if userId in self.latestTweets:
            prevTweet = self.latestTweets[userId]
            tweet = TweetObj(self.tweet_id, userId, tweetId, prevTweet)
            self.latestTweets[userId] = tweet
        else:
            tweet = TweetObj(self.tweet_id, userId, tweetId, None)
            self.latestTweets[userId] = tweet

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        import heapq
        heap = []
        if userId not in self.following:
            return []
        followingUsers = self.following[userId]
        followingUsers.add(userId)
        for following_id in followingUsers:
            if following_id in self.latestTweets:
                latestTweet = self.latestTweets[following_id]
                tweetTuple = (-latestTweet.tweet_id, latestTweet.tweetContext, latestTweet.prevTweet)
                heapq.heappush(heap, tweetTuple)
        result = []
        for _ in range(10):
            if not heap:
                break
            tweetTuple = heapq.heappop(heap)
            result.append(tweetTuple[1])
            if tweetTuple[2]:
                newTweet = tweetTuple[2]
                newTweetTuple = (-newTweet.tweet_id, newTweet.tweetContext, newTweet.prevTweet)
                heapq.heappush(heap, newTweetTuple)
        return result

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = set([followeeId])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.following and followerId != followeeId:
            self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)