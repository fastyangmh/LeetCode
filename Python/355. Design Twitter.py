import heapq


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []

        users = self.following.get(userId, set()) | {userId}

        for uid in users:
            if uid not in self.tweets:
                continue

            time, tweet_id = self.tweets[uid][-1]
            idx = len(self.tweets[uid]) - 1

            heapq.heappush(heap, (time, tweet_id, uid, idx))

        while heap and len(res) < 10:
            time, tweet_id, uid, idx = heapq.heappop(heap)
            res.append(tweet_id)

            if idx > 0:
                next_time, next_tweet_id = self.tweets[uid][idx - 1]

                heapq.heappush(heap, (next_time, next_tweet_id, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.following.setdefault(followerId, set()).discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
