import unittest
from strategy import BubbleSort, InsertionSort, QuickSort, Sorter


class TestSortStrategy(unittest.TestCase):
    def setUp(self):
        self.data = [6, 9, 3, 8, 2]

    def test_BubbleSortInstance(self):
        bubble_sort_strategy = BubbleSort()
        self.assertIsInstance(bubble_sort_strategy, BubbleSort)

    def test_InsertionSortInstance(self):
        insertion_sort_strategy = InsertionSort()
        self.assertIsInstance(insertion_sort_strategy, InsertionSort)

    def test_QuickSortSorting(self):
        quick_sort_strategy = QuickSort()
        sorter = Sorter(quick_sort_strategy)
        sorted_data = sorter.sort(self.data)
        self.assertEqual(sorted_data, [2, 3, 6, 8, 9])

    def test_BubbleSortSorting(self):
        bubble_sort_strategy = BubbleSort()
        sorter = Sorter(bubble_sort_strategy)
        sorted_data = sorter.sort(self.data)
        self.assertEqual(sorted_data, [2, 3, 6, 8, 9])


if __name__ == '__main__':
    unittest.main()
