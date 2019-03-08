
import unittest

def first(a):
    return(len(a))
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def nameSaying(self):
        return(self.name)



class Testing(unittest.TestCase):
    def test_nameSaying(self):
        person = Person("soroush",36)
        assert person.nameSaying()=="soroush"


if __name__ == '__main__':
    unittest.main()
