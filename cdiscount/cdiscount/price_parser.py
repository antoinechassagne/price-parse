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
    url = "https://www.cdiscount.com/f-0-" + sku + ".html"
    request = requests.get(url)

    if (request.status_code != 200):
        return False

    soup = BeautifulSoup(request.text, "html.parser")
    price = float(soup.find_all("span", {"class":"fpPrice price jsMainPrice jsProductPrice hideFromPro"})[0]["content"])

    return price
  