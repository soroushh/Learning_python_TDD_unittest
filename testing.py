import unittest

def first(a):
    return(len(a))

class Testing(unittest.TestCase):

    def test_first(self):
        self.assertEqual(first("hel"),3)

if __name__ == '__main__':
    unittest.main()
