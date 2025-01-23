import unittest
from app import sum

class Tests(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)

if __name__ == '__main__':
    unittest.main()