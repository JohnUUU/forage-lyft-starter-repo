import sys
sys.path.append('../../')

import unittest
from tires.model.carrigan_tires import CarriganTires

class TestWilloughbyEngine(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        sensor_data_one = [1, 0, 0.5, 0.8]
        tires_one = CarriganTires(sensor_data_one)
        sensor_data_two = [0.9, 0.33, 0.3, 0.25]
        tires_two = CarriganTires(sensor_data_two)
        self.assertTrue(tires_one.tires_should_be_serviced())
        self.assertTrue(tires_two.tires_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self): 
        sensor_data = [0.89, 0.89, 0.899, 0.8999]
        tires = CarriganTires(sensor_data)
        self.assertFalse(tires.tires_should_be_serviced())
    
if __name__ == '__main__':
    unittest.main()