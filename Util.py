import MemeRequest
import json
import subprocess

def callCURLScripts():
    '''Uses a cURL script to send a GET request to the reddit api'''
    for subreddit in MemeRequest.MemeRequest.subreddits:
        subprocess.call('bash request_reddit.sh ' + subreddit, shell=True)

def loadJsonFile(filename):
    try:
        f = open(filename, 'r')
        s = f.read()
        f.close()
        data = json.loads(s)
        return data
    except IOError:
        print("Unable to open the json file")