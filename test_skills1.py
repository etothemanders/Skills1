import skills1
import unittest

class TestSkills1(unittest.TestCase):
    
    def setUp(self):
        self.int_list = [-1, 0, 1, 2]
        self.str_list = ["Four", "score", "and", "seven", "years", "ago", "our", "forefathers", "brought", "forth", "on", "this", "continent"]
        unordered_ints = [5, 27, -1, 0, 23, -8, 2]
    
    def test_all_odd(self):
        self.assertEqual(skills1.all_odd(self.int_list), [-1, 1])
    
    def test_all_even(self):
        self.assertEqual(skills1.all_even(self.int_list), [0, 2])
    
    def test_long_words(self):
        self.assertEqual(skills1.long_words(self.str_list), ["Four", "score", "seven", "years", "forefathers", "brought", "forth", "this", "continent"])
    
    def test_smallest(self):
        self.assertEqual(skills1.smallest(self.int_list), -1)
    
    def test_largest(self):
        self.assertEqual(skills1.largest(self.int_list), 2)
    
    def test_halvesies(self):
        self.assertEqual(skills1.halvesies(self.int_list), [-1, 0, 0, 1])
        
    def test_word_lengths(self):
        pass
        
    def test_sum_numbers(self):
        pass
        
    def test_mult_numbers(self):
        pass
        
    def test_join_strings(self):
        pass
        
    def test_average(self):
        pass
        
    # no tearDown() method needed for this suite        

if __name__ == "__main__":
    unittest.main()