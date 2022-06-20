import sys
sys.path.append('../../')

import unittest
from engine.model.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 13012
        current_mileage = last_service_mileage + 30000
        engine_one = CapuletEngine(current_mileage, last_service_mileage)
        current_mileage = last_service_mileage + 30001 
        engine_two = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine_one.engine_should_be_serviced())
        self.assertTrue(engine_two.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self): 
        last_service_mileage = 112934
        current_mileage = last_service_mileage + 20000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()