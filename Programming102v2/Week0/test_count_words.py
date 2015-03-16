import unittest
from count_words import count_words


class TestCountWords(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(3, len(count_words(["apple", "banana", "apple", "pie"])))
        self.assertEqual(2, len(count_words(["python", "python", "python", "ruby"])))


if __name__ == '__main__':
    unittest.main()
