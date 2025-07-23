import requests

resp = requests.get("http://127.0.0.1:5656/stocks/allStock/")
print(resp.json())