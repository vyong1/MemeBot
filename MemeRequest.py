import subprocess
import json
import datetime
import shutil
import requests
import random
import RateLimiter
import PreviousRequestTime

'''
    Black box diagram of this class

                  _______________
                 |               |
    giveMeme() --|   MemeRequest |-- post
                 |_______________|

    Where post = {
        "title" : someTitle, 
        "url" : someUrl, 
        "nsfw" : True/False
        }
'''


class MemeRequest:
    '''
    Requests memes from various subreddits, but limits the
    rate of requests to 1 every 30 min.
    This class is instantiated per request.
    '''

    subreddits = [
        'dankmemes',
        'me_irl',
        'MemeEconomy',
        'ProgrammerHumor',
        'hmmm'
    ]

    RATE_LIMIT = 1800 # 1800 seconds = 30 min

    def __init__(self):
        self.time_of_creation = datetime.datetime.now()
        self.rateLimiter = RateLimiter.RateLimiter(MemeRequest.RATE_LIMIT)
        self.prevReqTime = PreviousRequestTime.PreviousRequestTime("files/prev_req_time.txt")

    def __parseMemes(self):
        '''Parses the json response'''
        memeDict = {}
        for subreddit in MemeRequest.subreddits:
            # Read in the cached json response
            filename = 'files/CachedRequests/' + subreddit + '.json'
            f = open(filename, 'r')
            s = f.read()
            f.close()
            data = json.loads(s)
            # Parse the json response
            memes = {}
            for i in range(0, 25):
                title = data['data']['children'][i]['data']['title']
                url = data['data']['children'][i]['data']['url']
                nsfw = (data['data']['children'][i]['data']['thumbnail'] == 'nsfw')
                memes[i] = {
                    "title" : title,
                    "url" : url,
                    "nsfw" : nsfw
                }
            memeDict[subreddit] = memes
        jsonString = json.dumps(memeDict)

        f = open('files/MemeDict.json', 'w')
        f.write(jsonString)
        f.close()
                
    def __requestPosts(self):
        '''Uses a cURL script to send a GET request to the reddit api'''
        for subreddit in MemeRequest.subreddits:
            subprocess.call('bash request_reddit.sh ' + subreddit, shell=True)
    
    def __request(self):
        '''Request memes (if the rate limiter allows)'''
        # Calculate the delta time
        prev_datetime = self.prevReqTime.get()
        delta_seconds = (self.time_of_creation - prev_datetime).total_seconds()
        # Limit the rate
        canRequest = self.rateLimiter.canAct(delta_seconds)
        # If request available, then send it
        if(canRequest):
            print("Request sent")
            self.__requestPosts()
            self.__parseMemes()
            self.prevReqTime(self.time_of_creation)
        # True => A request has been sent
        # False => A request has not been sent
        return canRequest

    def giveMeme(self):
        # Request the latest (dankest) memes
        self.__request()
        # Open up the meme dictionary
        f = open('files/MemeDict.json', 'r')
        s = f.read()
        f.close()
        memeDict = json.loads(s)

        # Pick a random sub and a random post from that sub
        sub = MemeRequest.subreddits[random.randint(0, len(MemeRequest.subreddits) - 1)]
        postnum = random.randint(0, 24)
        post = memeDict[sub][str(postnum)]
        # Return the post
        return post