import json
from urllib import urlopen

def goInside( str ):
    link = urlopen(str).read()
    tree = json.loads(link)
    print '"Name":', tree['name']
    print '"Email":', tree['email']
    print '"Location":', tree['location']
    print

def saveLink( str ):
    baseLink = "https://api.github.com/users/"
    baseLinkV2 = "?client_id=abce3e0cd57466d1d55c&client_secret=ccfdf4e7e7b36d1aca21a43f5d381a55c9c4e084"
    baseLink = baseLink + str + baseLinkV2
    goInside(baseLink)

url = urlopen('https://api.github.com/search/repositories?q=java&sort=stars&order=desc').read()
result = json.loads(url)  # result is now a dict
cicle=0

print "Get most recent authors of Trending GitHub Repositories:"

while True:
    try:
        print '"Author":', result['items'][cicle]['owner']['login']
        saveLink( result['items'][cicle]['owner']['login'] )
        cicle += 1
    except:
        break
