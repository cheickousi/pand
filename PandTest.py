import unittest

from pand import Board, Solver


class MyTestCase(unittest.TestCase):
    def test_something(self):
        cities = [12, 15, 35, 100, 200, 1000, 10000]

        for city in cities:

            for epicenter in range(city):
                print('city and epicenter are: ', city, epicenter)
                board = Board(city, epicenter)
                solve = Solver(board).solve()
                if solve != epicenter:
                    print(solve, epicenter)
                print(solve, epicenter)
                self.assertEqual(solve, epicenter)  # add assertion here


if __name__ == '__main__':
    unittest.main()
