#import requests
import time
import asyncio
import httpx

async def fetch():
    urls = [
        "http://books.toscrape.com/catalogue/category/books/travel_2/index.html",
        "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
        "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html",
        "http://books.toscrape.com/catalogue/category/books/classics_6/index.html",
        "http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
        "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
        "http://books.toscrape.com/catalogue/category/books/music_14/index.html",
        "http://books.toscrape.com/catalogue/category/books/default_15/index.html",
        "http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html",
        "http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html",
        "http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html",
        "http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html",
        "http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html"
    ]
    #results = [requests.get(url) for url in urls]

    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in urls]
        results = await asyncio.gather(*reqs)

    print(results)


start = time.perf_counter()
asyncio.run(fetch())
end = time.perf_counter()

print(end-start)
