from urllib import urlopen
import json

bestrepositories = urlopen('https://api.github.com/search/repositories?q=java&sort=stars&order=desc')
result=json.load(bestrepositories)

def Link(str):
    baseLink = "https://api.github.com/users/"
    baseLinkV2 = "?client_id=abce3e0cd57466d1d55c&client_secret=ccfdf4e7e7b36d1aca21a43f5d381a55c9c4e084"
    baseLink = baseLink + str + baseLinkV2
    goProfile(baseLink)

def goProfile(str):

    result = urlopen(str).read()
    newTree=json.loads(result)
    print "name:", newTree['name']
    print "email", newTree['email']
    print ""


print "Get most recent authors of trending GitHub Repositories"
i = 0

while True:
    print result['items'][i]['owner']['login']
    Link( result['items'][i]['owner']['login'])
    i+= 1
