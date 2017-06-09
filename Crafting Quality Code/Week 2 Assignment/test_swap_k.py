import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_complete_list(self):
        """ 
        Test swap_k such that the entire list is swap completely
        where k == len(L) // 2 on an even lengthed string
    
        """
        list_input = [1,2,3,4,5,6,7,8]
        a1.swap_k(list_input, 4)
        
        list_output = [5,6,7,8,1,2,3,4]
        
        self.assertEqual(list_input,list_output)
        
    def test_swap_k_no_swap(self):
        """ 
        Test swap_k such that there is no swap.
    
        """
        list_input = [1,2,3,4,5,6,7,8]
        a1.swap_k(list_input, 0)
        
        list_output = [1,2,3,4,5,6,7,8]
        
        self.assertEqual(list_input,list_output)        
        
    def test_swap_k_list_empty(self):
        """ 
        Test swap_k such that there is no list.
    
        """
        list_input = []
        a1.swap_k(list_input, 0)
        
        list_output = []
        
        self.assertEqual(list_input,list_output)    
        
    def test_swap_k_one_only(self):
        """ 
        Test swap_k such that it is a swap of 1.
    
        """
        list_input = [1,2,3,4,5,6,7,8]
        a1.swap_k(list_input, 1)
        
        list_output = [8,2,3,4,5,6,7,1]
        
        self.assertEqual(list_input,list_output)  
        
    def test_swap_k_normal(self):
        """ 
        Test swap_k such that it is a swap of 2.
    
        """
        list_input = [1,2,3,4,5,6,7,8]
        a1.swap_k(list_input, 2)
        
        list_output = [7,8,3,4,5,6,1,2]
        
        self.assertEqual(list_input,list_output)  
        
        
if __name__ == '__main__':
    unittest.main(exit=False)
