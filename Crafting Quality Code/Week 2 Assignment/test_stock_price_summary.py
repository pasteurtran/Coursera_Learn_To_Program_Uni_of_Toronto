import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_zero(self):
        """ 
        Test stock_price_summary for a day with no movements.
    
        """
        actual = a1.stock_price_summary([0.0, 0.0, 0.0, 0.0])
        
        expected = (0.0, 0.0)
        
        self.assertEqual(actual,expected)
    
    
    def test_stock_price_summary_market_crash(self):
        """ 
        Test stock_price_summary for a day where there is no 
        gains in the market. Everything is negative, with no positive
        gains
    
        """
        actual = a1.stock_price_summary([-0.9, -0.02, -0.14, -0.7, -0.3, -0.5, -0.01])
        
        expected = (0.0, -2.57)
        
        self.assertEqual(actual,expected)
        
    def test_stock_price_summary_bull_market(self):
        """ 
        Test stock_price_summary for a day where there is ALL 
        gains in the market. Everything is positive, with no negatives.
    
        """
        actual = a1.stock_price_summary([0.9, 0.02, 0.14, 0.7, 0.3, 0.5, 0.01])
        
        expected = (2.57, 0.0)
        
        self.assertEqual(actual,expected)
        
    def test_stock_price_normal_day(self):
        """ 
        Test stock_price_summary for a mix of negative and positive.
    
        """
        actual = a1.stock_price_summary([0.9, 0.02, -0.14, 0.7, -0.3, -0.5, 0.01])
        
        expected = (1.63, -0.94)
        
        self.assertEqual(actual,expected)
    

if __name__ == '__main__':
    unittest.main(exit=False)
