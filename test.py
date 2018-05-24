import MemeRequest
import subprocess
import json
# https://codebeautify.org/jsonviewer

def install():
    # Initializes the directory so that MemeBot.py works
    pass

def clean():
    pass

# https://imgur.com/k6n4FVS
# https://i.imgur.com/k6n4FVS.jpg
url = 'https://imgur.com/k6n4FVS'
if "imgur" in url:
    url = url[0:8] + 'i.' + url[8:] + '.jpg'
print(url)