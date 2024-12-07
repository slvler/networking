import requests

with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

to_check = [
    "http://books.toscrape.com/",
    "https://eksisozluk.com/7-aralik-2024-besiktas-fenerbahce-maci--7878264",
    "https://eksisozluk.com/3-temmuz-2011-futbolda-sike-sorusturmasi--2904882",
    "https://eksisozluk.com/turkiye-hiristiyan-olsaydi-olabilecekler--2546941"
]

counter = 0

for site in to_check:
    try:
        print(f'the proxy: {proxies[counter]}')
        proxies = {
            "http": proxies[counter],
            "https": proxies[counter],
        }
        print(proxies)
        res = requests.get(site, proxies=proxies)
    except:
        print("Failed")
    finally:
        counter += 1
        counter % len(proxies)

