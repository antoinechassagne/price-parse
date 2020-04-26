from typing import Union
import requests
from bs4 import BeautifulSoup

"""
This function extracts the price from a Cdiscount product page.

Parameters:
    sku (str): The product reference

Returns:
    float: The product price
    bool: False if something went wrong
"""


def parse_price(sku: str) -> Union[float, bool]:
    if not isinstance(sku, str):
        return False

    url = "https://www.cdiscount.com/f-0-" + sku + ".html"
    request = requests.get(url)

    if (request.status_code != 200):
        return False

    soup = BeautifulSoup(request.text, "html.parser")
    price_box = soup.find_all("span", {"class": "fpPrice price jsMainPrice jsProductPrice hideFromPro"})

    if (not len(price_box)):
        return False

    price = float(price_box[0]["content"])
    return price
