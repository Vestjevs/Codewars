import numpy as np
import requests
from lxml import html
import json
import yaml
from bs4 import BeautifulSoup
import re

# https://yummybook.ru/recept/taramosalata

# https://yummybook.ru/category/recepty-salatov#view-mode-list

site_url = "https://yummybook.ru/"

# class_='b-rec-head' -> dish name


# class_="b-all-its-link" -> category at main url

# class_="b-ck-filter-num-find" -> count pages at /category/special-tratata

# class_="b-rec-head-v2" -> by this we can get dish name and can get path to each recipe

# each website with recipe
# class_='b-item col-lg-12 col-md-12 col-sm-12 col-xs-12' -> by this class parse at site of recipe
# class_='b-text' -> step for cooking


#
# for i in range(0, len(soup.find_all(class_="b-inner")), +2):
#     result = re.findall(r'\/.+\/.+"', str(soup.find_all(class_="b-all-its-link")[i]))
#
#     string = str(result).split('/')[-1].split(' ')
#
#     category_url = "https://yummybook.ru/category/{}".format(string[0][:-3])
#
#     category_data = requests.get(category_url)
#
#     category_soup = BeautifulSoup(category_data.text, 'html.parser')
#
#     for elem in category_soup.find_all(class_='b-ck-filter-num-find'):
#         count = re.findall(r'<i>.+</i>', str(elem))
#
#         count_dish = int(count[0][3:-4])
#
#         # count of page
#         page = count_dish // 24 + 1
#
#         for i in range(1, page + 1):
#             category_url_page_i = '{}/page/{}'.format(category_url, i)
#
#             category_data_page_i = requests.get(category_url_page_i)
#
#             print(category_data_page_i.status_code)
#


# url = "https://yummybook.ru/category/recepty-dlya-multivarok/page/1"
#
# req1 = requests.get(url)
#
# soup1 = BeautifulSoup(req1.text, 'html.parser')

# for dish in soup1.find_all(class_="b-rec-head-v2"):
#     result1 = re.findall(r'<a href=".+">.+</a>', str(dish))
#     href = str(result1[0][9:-4]).split('">')
#     print(href[0] + " || " + href[1])


dish_url = "https://yummybook.ru/recept/bulgur-s-gribami-v-multivarke"

req2 = requests.get(dish_url)

dish_soup = BeautifulSoup(req2.text, 'html.parser')

# for ingredient in str(dish_soup.find_all(class_="b-item col-lg-12 col-md-12 col-sm-12 col-xs-12")).split('li'):
#     result2 = re.findall(r'>.+<', str(ingredient))
#     if len(result2) != 0:
#       print(str(result2)[3:-3]) this print ingredients


#
# for step in dish_soup.find_all(class_="b-text"):
#     result3 = re.findall(r'>.+<', str(step))
#     print(str(result3[1])[1:-1])

url_web_site = "https://yummybook.ru"


# 1 layer
def scrap_it():
    request = requests.get(site_url)

    soup = BeautifulSoup(request.text, 'html.parser')

    for i in range(0, len(soup.find_all(class_="b-inner")), +2):
        result = re.findall(r'\/.+\/.+"', str(soup.find_all(class_="b-all-its-link")[i]))

        string = str(result).split('/')[-1].split(' ')

        special_category = "{}/category/{}".format(url_web_site, string[0][:-3])

        print(string[0][:-3])

        request = requests.get(special_category)

        special_category_soup = BeautifulSoup(request.text, 'html.parser')

        for elem in special_category_soup.find_all(class_='b-ck-filter-num-find'):
            count = re.findall(r'<i>.+</i>', str(elem))

            count_dish = int(count[0][3:-4])
            # count_of page
            count_of_page = count_dish // 24 + 1


def ingredients_and_steps(special_dish_url1):
    request = requests.get(special_dish_url1)

    dish_soup = BeautifulSoup(request.text, 'html.parser')

    ingredients = []
    if str(dish_soup.find_all(class_="b-item col-lg-12 col-md-12 col-sm-12 col-xs-12")).split('li') != 0:
        for ingredient in str(
                dish_soup.find_all(class_="b-item col-lg-12 col-md-12 col-sm-12 col-xs-12")).split('li'):
            result2 = re.findall(r'>.+<', str(ingredient))
            if len(result2) != 0:
                ingredients.append(str(result2)[3:-3])
                # print({"{}".format(i): str(result2)[3:-3]})
    elif str(dish_soup.find_all(class_="b-item col-lg-6 col-md-6 col-sm-6 col-xs-12")).split('li') != 0:
        for ingredient in str(
                dish_soup.find_all(class_="b-item col-lg-6 col-md-6 col-sm-6 col-xs-12")).split('li'):
            result2 = re.findall(r'>.+<', str(ingredient))

            if len(result2) != 0:
                ingredients.append(str(result2)[3:-3])

    # this print ingredients
    i = 0
    steps = []
    for step in dish_soup.find_all(class_='b-text'):
        result3 = re.findall(r'>.+<', str(step))

        if len(result3) == 2:
            steps.append(str(result3[1])[1:-1])
        elif len(result3) == 1:
            steps.append(str(result3[0])[1:-1])

    return ingredients, steps


def get_list_of_special_dishes(category_url_page_i):
    request = requests.get(category_url_page_i)
    soup = BeautifulSoup(request.text, 'html.parser')

    list_of_special_dishes = []
    for dish in soup.find_all(class_="b-rec-head-v2"):
        result1 = re.findall(r'<a href=".+">.+</a>', str(dish))
        href = str(result1[0][9:-4]).split('">')

        # print(href[0] + " || " + href[1])

        special_dish_url = '{}{}/'.format(url_web_site, href[0])
        ingredients, steps = ingredients_and_steps(special_dish_url)

        special_dict = {
            'name': '{}'.format(href[1]),
            'ingredients': [str(elem) for elem in ingredients],
            'steps': [str(elem) for elem in steps]

        }

        list_of_special_dishes.append(special_dict)

    return list_of_special_dishes


def create_special_category(special_category_name, url_category, count_of_page):
    special_category = []
    for i in range(1, count_of_page + 1):
        category_url_page_i = '{}/page/{}'.format(url_category, i)

        special_category.append(get_list_of_special_dishes(category_url_page_i))

    menu = {
        '{}'.format(special_category_name): special_category
    }

    return menu


# newdict = {
#     'special_category': get_list_of_special_dishes('https://yummybook.ru/category/pervye-blyuda/page/1')
# }

# menu = {
#     'menu': create_special_category('https://yummybook.ru/category/pervye-blyuda/', 16)
# }
#
    with open('saladsRecipes.json', 'w', encoding='utf-8') as f:
        json.dump(create_special_category('Рецепты салатов', 'https://yummybook.ru/category/recepty-salatov', 24 ), f,
                  indent=4,
                  ensure_ascii=False)

# print(get_list_of_special_dishes('https://yummybook.ru/category/pervye-blyuda/page/4'))
