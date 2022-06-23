import sys
sys.path.append('../../')

import unittest
from tires.model.octoprime_tires import OctoprimeTires

class TestWilloughbyEngine(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensor_data_one = [1, 0, 0.5, 1.5]
        tires_one = OctoprimeTires(sensor_data_one)
        sensor_data_two = [2, 2, 1, 0]
        tires_two = OctoprimeTires(sensor_data_two)
        self.assertTrue(tires_one.tires_should_be_serviced())
        self.assertTrue(tires_two.tires_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self): 
        sensor_data = [0.7, 0.7, 0.7, 0.7]
        tires = OctoprimeTires(sensor_data)
        self.assertFalse(tires.tires_should_be_serviced())
    
if __name__ == '__main__':
    unittest.main()