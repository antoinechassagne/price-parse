from flask import Flask, request
from cdiscount.price_parser import parse_price

app = Flask(__name__)

@app.route('/')
def main():
    sku = request.args.get('sku')
  
    price = parse_price(sku)
    if (not price):
        return "Une erreur s'est produite."
  
    return str(price)