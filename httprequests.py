import requests

res = requests.get("http://yandex.ru/search", params={"text": "Python"})

print(res.status_code)
print(res.headers["Content-Type"])
print(res.url)
print(res.text)
