import sys
sys.path.append('../../')

import unittest
from datetime import datetime
from battery.model.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date_one = current_date.replace(
            year=current_date.year - 5)
        battery_one = NubbinBattery(current_date, last_service_date_one)
        self.assertTrue(battery_one.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())

if __name__ == '__main__':
    unittest.main()
    