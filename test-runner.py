import unittest
import importlib

class TestAssignmentFive(unittest.TestCase):
    def test_01(self):
        square_sqrt_args = asgmt.SquareSqrtArgs()
        self.assertEqual(square_sqrt_args.square_args(0, 1, 2), [0, 1, 4])
        self.assertEqual(square_sqrt_args.sqrt_args(0, 1, 4), [0.0, 1.0, 2.0])
        self.assertEqual(square_sqrt_args.square_args(3, 4, 5), [9, 16, 25])
        self.assertEqual(square_sqrt_args.sqrt_args(9, 16, 25), [3.0, 4.0, 5.0])
    def test_02(self):
        min_max_finder = asgmt.MinMaxFinder([2, 3, 5, 7, 11, 11, 7, 5, 3, 2])
        self.assertIsInstance(min_max_finder.integer_list, list)
        self.assertEqual(min_max_finder.find_min(), 2)
        self.assertEqual(min_max_finder.find_max(), 11)
        self.assertEqual(min_max_finder.find_idxmin(), [0, 9])
        self.assertEqual(min_max_finder.find_idxmax(), [4, 5])
        min_max_finder = asgmt.MinMaxFinder([10, 9, 8, 6, 4, 1, 1, 4, 6, 8, 9, 10])
        self.assertIsInstance(min_max_finder.integer_list, list)
        self.assertEqual(min_max_finder.find_min(), 1)
        self.assertEqual(min_max_finder.find_max(), 10)
        self.assertEqual(min_max_finder.find_idxmin(), [5, 6])
        self.assertEqual(min_max_finder.find_idxmax(), [0, 11])
    def test_03(self):
        cd = asgmt.CommonDivisors(3, 6)
        self.assertEqual(len(cd.x_divisors), 2)
        self.assertEqual(len(cd.y_divisors), 4)
        self.assertEqual(len(cd.get_common_divisors()), 2)
        cd = asgmt.CommonDivisors(4, 8)
        self.assertEqual(len(cd.x_divisors), 3)
        self.assertEqual(len(cd.y_divisors), 4)
        self.assertEqual(len(cd.get_common_divisors()), 3)
    def test_04(self):
        pj = asgmt.PrimeJudger(1)
        self.assertEqual(len(pj.get_divisors()), 1)
        self.assertFalse(pj.is_prime())
        pj = asgmt.PrimeJudger(2)
        self.assertEqual(len(pj.get_divisors()), 2)
        self.assertTrue(pj.is_prime())
        pj = asgmt.PrimeJudger(4)
        self.assertEqual(len(pj.get_divisors()), 3)
        self.assertFalse(pj.is_prime())
    def test_05(self):
        zip_codes_json = asgmt.import_zip_codes_json()
        self.assertIsInstance(zip_codes_json, list)
        self.assertEqual(len(zip_codes_json), 378)
    def test_06(self):
        self.assertEqual(asgmt.lookup_zip_code("臺北市", "中正區"), 100)
        self.assertEqual(asgmt.lookup_zip_code("基隆市", "中正區"), 202)
        self.assertEqual(asgmt.lookup_zip_code("臺北市", "中山區"), 104)
        self.assertEqual(asgmt.lookup_zip_code("基隆市", "中山區"), 203)
        self.assertEqual(asgmt.lookup_zip_code("臺北市", "大安區"), 106)
        self.assertEqual(asgmt.lookup_zip_code("臺中市", "大安區"), 439)
        self.assertEqual(asgmt.lookup_zip_code("臺北市", "內湖區"), 114)
        self.assertEqual(asgmt.lookup_zip_code("臺北市", "文山區"), 116)
    def test_07(self):
        self.assertEqual(asgmt.lookup_county_town(100), ("臺北市", "中正區"))
        self.assertEqual(asgmt.lookup_county_town(202), ("基隆市", "中正區"))
        self.assertEqual(asgmt.lookup_county_town(104), ("臺北市", "中山區"))
        self.assertEqual(asgmt.lookup_county_town(203), ("基隆市", "中山區"))
        self.assertEqual(asgmt.lookup_county_town(106), ("臺北市", "大安區"))
        self.assertEqual(asgmt.lookup_county_town(439), ("臺中市", "大安區"))
        self.assertEqual(asgmt.lookup_county_town(114), ("臺北市", "內湖區"))
        self.assertEqual(asgmt.lookup_county_town(116), ("臺北市", "文山區"))
    def test_08(self):
        countries_json = asgmt.import_countries_json()
        self.assertIsInstance(countries_json, list)
        self.assertEqual(len(countries_json), 249)
    def test_09(self):
        self.assertEqual(asgmt.lookup_country_iso_codes("Taiwan"), ('TW', 'TWN'))
        self.assertEqual(asgmt.lookup_country_iso_codes("Japan"), ('JP', 'JPN'))
        self.assertEqual(asgmt.lookup_country_iso_codes("Lithuania"),  ('LT', 'LTU'))
        self.assertEqual(asgmt.lookup_country_iso_codes("Slovenia"), ('SI', 'SVN'))
        self.assertEqual(asgmt.lookup_country_iso_codes("Czechia"),  ('CZ', 'CZE'))
        self.assertEqual(asgmt.lookup_country_iso_codes("United States of America (the)"), ('US', 'USA'))
    def test_10(self):
        self.assertEqual(asgmt.lookup_country_name("TW"), 'Taiwan')
        self.assertEqual(asgmt.lookup_country_name("TWN"), 'Taiwan')
        self.assertEqual(asgmt.lookup_country_name("JP"), 'Japan')
        self.assertEqual(asgmt.lookup_country_name("JPN"), 'Japan')
        self.assertEqual(asgmt.lookup_country_name("LT"), 'Lithuania')
        self.assertEqual(asgmt.lookup_country_name("LTU"), 'Lithuania')
        self.assertEqual(asgmt.lookup_country_name("CZ"), 'Czechia')
        self.assertEqual(asgmt.lookup_country_name("CZE"), 'Czechia')
        self.assertEqual(asgmt.lookup_country_name("US"), 'United States of America (the)')
        self.assertEqual(asgmt.lookup_country_name("USA"), 'United States of America (the)')

asgmt = importlib.import_module("asgmt-five")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFive)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))