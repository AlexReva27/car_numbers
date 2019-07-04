import os, keyboard, unittest
#from car_numbers import func


class TestNumbers(unittest.TestCase):
    
    def setUp(self):
        self.input = "  a   "
        self.file = "c138mt54 a198mm97 m962cn17 c138mt54 a122cn13"

    def test_strip(self):
        guess = "  abc   " 
        self.assertEqual (guess.strip(), "abc")

    print ("Тесты еще в процессе написания")

if __name__ == '__main__':
    unittest.main()

