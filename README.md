# Price parser

Parse a Cdiscount product price.

## Installation

### Clone the repository

`git clone git@github.com:antoinechassagne/price-parser.git`

### Build the docker image

`docker build --tag price_parser .`

### Run the container

`docker run --name price_parser -p 8080:8080 price_parser`

### Now visist

`http://localhost:8080`

## Usage

Hit the `/` endpoint with a query param `sku` coresponding to a Cdiscount product reference.

### Example

`http://localhost:8080/?sku=pan5025232500635`
