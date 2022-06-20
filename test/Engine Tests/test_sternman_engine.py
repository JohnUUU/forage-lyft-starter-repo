import sys
sys.path.append('../../')

import unittest
from engine.model.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())
    
    def test_engine_should_not_be_serviced(self): 
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
    