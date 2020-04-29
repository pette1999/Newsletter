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
