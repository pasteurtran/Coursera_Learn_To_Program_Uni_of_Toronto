import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    
    def test_num_buses_equal_0(self):
        """ 
        Test num_buses wehre there are no people at all,
        meaning the result should expect 0 buses. 
    
        """
        actual = a1.num_buses(0)
        
        expected = 0
        
        self.assertEqual(actual,expected)
        
    def test_num_buses_under(self):
        """ 
        Test num_buses between 1-49. 
    
        """
        actual = a1.num_buses(45)
        
        expected = 1
        
        self.assertEqual(actual,expected)
    
    def test_num_buses_alot(self):
        """ 
        Test num_buses wehre there are are a lot of people
    
        """
        actual = a1.num_buses(248)
        
        expected = 5
        
        self.assertEqual(actual,expected)
    
    def test_num_buses_equal_one(self):
        """ 
        Test num_buses where the numebr is exaclty 50
    
        """
        actual = a1.num_buses(50)
        
        expected = 1
        
        self.assertEqual(actual,expected)
        
    def test_num_buses_just_more(self):
        """ 
        Test num_buses between 51-99
    
        """
        actual = a1.num_buses(57)
        
        expected = 2
        
        self.assertEqual(actual,expected)
    

if __name__ == '__main__':
    unittest.main(exit=False)
