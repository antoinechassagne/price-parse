import requests
from bs4 import BeautifulSoup

def parse_price(sku: str) -> float:
  url = "https://www.cdiscount.com/f-0-" + sku + ".html"
  request = requests.get(url)

  if (request.status_code != 200):
    return 0
  
  soup = BeautifulSoup(request.text, "html.parser")
  price = float(soup.find_all("span", {"class":"fpPrice price jsMainPrice jsProductPrice hideFromPro"})[0]["content"])

  return price
  