import unittest
from cdiscount.price_parser import parse_price

class PriceParserTest(unittest.TestCase):
    """Test cases for price_parser module"""
    
    """Test cases for price_parser.parse_price function"""
    def test_parse_price(self):
        """Should return the price as flaot for a good sku given"""
        sku = "del5397184246030"
        result = parse_price(sku)
        self.assertEqual(type(result), float)

        """Should return False for a bad sku given"""
        sku = "zdadzaa"
        result = parse_price(sku)
        self.assertFalse(result)

        """Should return False for a bad sku type given"""
        sku = False
        result = parse_price(sku)
        self.assertFalse(result)
        
        sku = True
        result = parse_price(sku)
        self.assertFalse(result)
 
        sku = [1, 2, 3]
        result = parse_price(sku)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
