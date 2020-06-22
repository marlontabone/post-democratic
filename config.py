import twitter

def getApi():
 #returning Twitter account credentials to allow script to upload statuses/media to twitter bot account
 return twitter.Api(consumer_key = "5JD1Xl8zz0vFu9URaCh6oJ5Os", consumer_secret = "JJ8txIr1mPAKdFRrFkwPUQvitaN2X9aiCddxWbPqDcvUuwwKT1", access_token_key = "1270840961954873344-JAa7Qn9TeFHUIRqiDB3SInlgKD5u4v", access_token_secret = "YcdlCJ4Cg30qstQhSNvCjViMytDGmwh39lycwkhhvZHoq")
