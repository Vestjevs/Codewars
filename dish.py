import json

from bs4 import BeautifulSoup
from pymongo import MongoClient
import re
import requests
import datetime
import pprint

site = "https://kedem.ru/recipe/soup/smuch/gribnoj-sup-iz-shampinonov/"
site1 = "https://kedem.ru/recipe/bakery/pie/pirog-na-smetane-s-yablokami/"
site2 = "https://kedem.ru/recipe/nyrecipe/salads/salat-vostorg/"
site3 = "https://kedem.ru/recipe/salads/gribi/salat-pushinka/"
site4 = "https://kedem.ru/recipe/bakery/pie/sharlotka-na-smetane/"
site5 = "https://kedem.ru/recipe/salads/eggc/salat-grecheskij/"


# NAME
def create_name(soup):
    name = str(str(soup.find_all(class_="h1")).split(">")[1])[:-4]
    return name


def create_ingredients(soup):
    ingredients = []
    for elem in soup.find_all(class_="ringlist"):
        for string in re.findall(r';">.+<\/span', str(elem)):
            ingredients.append("{} - {}".format(str(str(string).split('>')[1].split('<span')[0]).split("<a")[0],
                                                str(string).split('>')[-2].split("</span")[0]))
    return ingredients


def create_steps(soup):
    steps = []
    flag = True
    for elem in soup.find_all(class_="rtext"):
        for index in range(len(re.findall(r'p>.+<\/p', str(elem))) - 1):
            steps.append(str(re.findall(r'p>.+<\/p', str(elem))[index])[2:-3])
            if str(str(re.findall(r'p>.+<\/p', str(elem))[index])[2:-3]).find("<a href=\"") != -1:
                flag = False

    return steps, flag


def create_url(url):
    list_of_links = []
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    for elem in soup.find_all(class_="w-clearfix w-inline-block pgrblock"):
        list_of_links.append(
            "https://kedem.ru{}".format(str(re.findall(r'a href=".+\/"', str(elem))).split("\"")[1]))

    return list_of_links


def create_soup(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    return soup


def create_dish(url):
    tup = create_steps(create_soup(url))
    dish = {
        "name": create_name(create_soup(url)),
        "ingredients": create_ingredients(create_soup(url)),
        "steps": create_steps(create_soup(url))[0]
    }
    return dish, tup[1]


def create_menu(url):
    list_of_urls = create_url(url)
    list_of_dishes = []
    for url in list_of_urls:
        dish = create_dish(url)
        if dish[1]:
            list_of_dishes.append(dish[0])

    return {
        "Special_dishes": list_of_dishes
    }


links = ["https://kedem.ru/recipe/salads/", "https://kedem.ru/recipe/dishes/", "https://kedem.ru/recipe/snack/",
         "https://kedem.ru/recipe/bakery/"]

names = ["salads", "dishes", "snack", "bakery"]

for (link, name) in zip(links, names):
    with open('{}.json'.format(name), 'w', encoding='utf-8') as f:
        json.dump(create_menu(link), f,
                  indent=4,
                  ensure_ascii=False)
