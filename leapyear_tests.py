import unittest
import leapyear

class testCaseAdd(unittest.TestCase):
    def test_isLeap(self):
        self.assertEqual(palindrome.isLeap(2004), True)

    def test_edgeLeap(self):
        self.assertEqual(palindrome.isLeap(2000), False)

    def test_notLeap(self):
        self.assertEqual(palindrome.isLeap(2003), True)

if __name__ == '__main__':
    unittest.main()
