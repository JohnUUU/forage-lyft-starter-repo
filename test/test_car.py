import sys
sys.path.append('../')

import unittest
from datetime import datetime
from car import Car
from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_car_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_bad_battery_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_bad_engine_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory().create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
    
    def test_car_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 20000
        last_service_mileage = 0

        car = CarFactory().create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_car_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_bad_battery_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_bad_engine_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory().create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
    
    def test_car_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 50000
        last_service_mileage = 0

        car = CarFactory().create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


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


class TestRorschach(unittest.TestCase):
    def test_car_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 6)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_bad_battery_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_bad_engine_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 2)
        current_mileage = 60000
        last_service_mileage = 0

        car = CarFactory().create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
    
    def test_car_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 2)
        current_mileage = 50000
        last_service_mileage = 0

        car = CarFactory().create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_car_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_bad_battery_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 6)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory().create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_bad_engine_only(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory().create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
    
    def test_car_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 2)
        current_mileage = 20000
        last_service_mileage = 0

        car = CarFactory().create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
