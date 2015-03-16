import unittest
from prepare_meal import prepare_meal


class testPrepareMeal(unittest.TestCase):

    def test_prepare_meal(self):
        self.assertGreater(len(prepare_meal(15)), len(prepare_meal(5)))
        self.assertNotEqual(prepare_meal(5), prepare_meal(105))


if __name__ == '__main__':
    unittest.main()
