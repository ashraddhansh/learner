from googlesearch import search

query = "Best Python libraries for data science"
results = search(query, tld="com", lang="en", num=5, stop=3, pause=2)
for result in results:
    print(result)
