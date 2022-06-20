import sys
sys.path.append('../../')

import unittest
from datetime import datetime
from car_factory import CarFactory

class TestPalindrome(unittest.TestCase):
    def test_car_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_is_on = False

        car = CarFactory().create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_bad_battery_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_is_on = False

        car = CarFactory().create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_bad_engine_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        warning_light_is_on = True

        car = CarFactory().create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_car_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        warning_light_is_on = True

        car = CarFactory().create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    unittest.main()