from lxml import etree
import requests

result = requests.get("https://docs.python.org/3/")
print(result.status_code)
print(result.headers["Content-Type"])

parser = etree.HTMLParser()
root = etree.fromstring(result.text, parser)

for element in root.iter("a"):
    print(element, element.attrib)
