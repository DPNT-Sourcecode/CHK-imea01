from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

# import unittest
# from solutions.SUM import sum_solution

# class TestMartianRobots(unittest.TestCase):
#     def test_compute(self):
#         self.assertEqual(sum_solution.compute(2, 1), 3)

# if __name__ == '__main__':
#     unittest.main()


