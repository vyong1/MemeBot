import subprocess
import json
import datetime
import shutil
import requests
import random

# vyong note: this is pretty sloppily written without much planning

class MemeRequest:
    # Caches requests to DankMemes

    subreddits = [
        'dankmemes',
        'me_irl',
        'MemeEconomy',
        'ProgrammerHumor'
    ]

    def __init__(self):
        self.time_of_creation = datetime.datetime.now()

    def __get_prev_req_time(self):
        # Startup Function - gets the datetime of the previous request
        f = open('files/prev_req_time.txt', 'r')
        time_str = f.read()
        f.close()
        prev_datetime = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f')
        return prev_datetime

    def __determine_if_can_request(self):
        # Startup Function - limits requests to once per 30 min
        delta = self.time_of_creation - self.prev_req_time
        time_elapsed = delta.total_seconds()
        if(time_elapsed > 1500): # 1500 sec = 30 min
            return True
        else:
            return False

    def __read_memes(self):
        # Startup Function - Parses the json response and requests all the meme images
        for subreddit in MemeRequest.subreddits:
            filename = 'files/CachedRequests/' + subreddit + '.json'
            f = open(filename, 'r')
            s = f.read()
            f.close()

            data = json.loads(s)
            for i in range(0, 25):
                title = data['data']['children'][i]['data']['title']
                url = data['data']['children'][i]['data']['url']
                nsfw = (data['data']['children'][i]['data']['thumbnail'] == 'nsfw')
                response = requests.get(url, stream=True)
                with open('files/meme_pics/' + str(i) + '.png', 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
        
    def __request_posts(self, subreddit):
        # Submits a curl request to the reddit api
        subprocess.call('bash request_reddit.sh ' + subreddit, shell=True)

    def __update_prev_req_time(self):
        # Update prev_req_time.txt with this object's time of creation
        f = open('files/prev_req_time.txt', 'w')
        f.write(str(self.time_of_creation))
        f.close()
    
    def request(self):
        # Request memes (if allowed to)
        # Get the delta time between this request and the previous one
        self.prev_req_time = self.__get_prev_req_time()
        self.can_request = self.__determine_if_can_request()
        
        if(self.can_request):
            print("Request sent")
            self.__request_posts()
            self.__read_memes()
            self.__update_prev_req_time()

    def giveMeme(self):
        return 'files/meme_pics/' + str(random.randint(0, 24)) + '.png'