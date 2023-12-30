from googlesearch import search

query = input("what do you want to search?\n")
results = search(query, lang="en",num_results=15,sleep_interval=5)
for result in results:
    print(result)
