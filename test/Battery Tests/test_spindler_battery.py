import sys
sys.path.append('../../')

import unittest
from datetime import datetime
from battery.model.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date_one = current_date.replace(
            year=current_date.year - 4)
        battery_one = SpindlerBattery(current_date, last_service_date_one)
        self.assertTrue(battery_one.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())

if __name__ == '__main__':
    unittest.main()