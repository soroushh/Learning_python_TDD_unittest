import unittest
from unittest.mock import MagicMock
import unittest.mock

class Airport:
    def __init__ (self):
        self.planes = []

    def land(self,plane):
        self.planes.append(plane)
        plane.landed(self)



class TestingAirport(unittest.TestCase):
    def test_land(self):
        airport = Airport()
        plane = MagicMock()
        airport.land(plane)
        assert airport.planes == [plane]
        plane.landed.assert_called_with(airport)

if __name__ == '__main__':
    unittest.main()
