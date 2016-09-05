# Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-
Create word embeddings using all comments from the /r/politics subreddit for the period Jan-Apr 2016. Each 'word vector' is a 300 dimensional vector trained using the Word2Vec CBOW algorithm. (The comments are phrase collocated before training.)

You can find the Reddit Comments Dataset here: https://www.reddit.com/r/bigquery/wiki/datasets

**Modeled in Python**

##Some examples:

####Words the model thinks is most similar to 'bernie':

![Similar to 'bernie'](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/bernie.png?raw=true)

####Similar to 'hillary':

![Similar to 'hillary'](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/hillary.png?raw=true)

Reddit's preference for Bernie is already apparent!

####Let's make sure the model understands what a 'corrupt politician' means:

![Corrupt](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/corrupt%20politician.png?raw=true)

Seems like it does.

####Find similarities of the term 'corrupt politician' with Bernie and Hillary:

![Corrupt Politician](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/corrupt%20politician%20candidates.png?raw=true)

Haha! The actual values of the cosine similarities might be a little arbitrary, but who has the larger value definitely reflects Reddit's (and nearly everyone else's) sentiment.

####Similarly, to find the 'idealistic' candidate:

![Idealistic](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/idealistic.png?raw=true)

![Idealistic Candidate](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/idealistic%20candidates.png?raw=true)

Not surprising.

####I noticed pro-Bernie posts on the subreddit almost never linked to the mainstream media. There were certain sites that always made it to the front page, that were either one of the more independent news outlets, or right-wing websites that were pro-Bernie by virtue of being anti-Hillary:

![pro-Bernie News](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/freebeacon.png?raw=true)

####Searching for 'Vermont Senator' interestingly didn't bring up Bernie, but caught Patrick Leahy:

![Vermont Senator](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/vermont%20senator.png?raw=true)

####Using cosine distances, it's also possible to find exceptions in groups:

![Parties](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/parties.png?raw=true)

![Anchors](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/anchors.png?raw=true)

![Networks](https://github.com/sgrvinod/Word2Vec-on-Reddit-s-Politics-Subreddit-Jan-Apr-2016-/blob/master/examples/networks.png?raw=true)







