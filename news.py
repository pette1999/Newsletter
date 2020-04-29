import requests
import json
from newsapi import NewsApiClient
# pip install newsapi-python

# Stored the api key in a seperate file and read it through the file
# To protect the api key from leaking
f = open("api.txt", "r")
api = f.readline()

# url = ('http://newsapi.org/v2/top-headlines?'+ 
#        'country=us&' + 
#        api_key)
# response = requests.get(url).json()

# print(json.dumps(response, indent=2))

newsapi = NewsApiClient(api_key=api)

top_headlines = newsapi.get_top_headlines(country='us')

count = 0;
# empty list which will
# contain all trending news
results = []
urls = []
for article in top_headlines['articles']:
    results.append(article["title"])
    urls.append(article["url"])

for i in range(len(results)):
    # printing all trending news
    print(i + 1, results[i])
    print(urls[i])
    print('\n')



'''
# importing requests package
import requests


def NewsFromBBC():
    # BBC news api
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=c7aa00f89fc44825823f79ba0a3899ad"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []
    urls = []
    for ar in article:
        results.append(ar["title"])
        urls.append(ar["url"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])
        print(urls[i])

    # Driver Code

#function to get top headlines in the US
def allNews():
    # top headlines in the US api
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=c7aa00f89fc44825823f79ba0a3899ad')
    response = requests.get(url)
    article = response["articles"]
    
    results = []
    urls = []

    for ar in article:
        results.append(ar["title"])
        urls.append(ar["url"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])
        print(urls[i])

    #print(response.json())

if __name__ == '__main__':
    # function call
    #allNews()
    NewsFromBBC()
'''