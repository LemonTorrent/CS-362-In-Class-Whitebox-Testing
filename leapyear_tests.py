import unittest
import leapyear

class testCaseAdd(unittest.TestCase):
    def test_isLeap(self):
        self.assertEqual(leapyear.isLeap(2004), True)

    def test_edgeLeap(self):
        self.assertEqual(leapyear.isLeap(2100), False)

    def test_notLeap(self):
        self.assertEqual(leapyear.isLeap(2003), False)

if __name__ == '__main__':
    unittest.main()
