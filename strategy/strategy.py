from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        sorted_data = list(data)
        n = len(sorted_data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if sorted_data[j] > sorted_data[j + 1]:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
        return sorted_data

class QuickSort(SortStrategy):
    def sort(self, data):
        sorted_data = list(data)
        self._quick_sort(sorted_data, 0, len(sorted_data) - 1)
        return sorted_data

    def _quick_sort(self, data, low, high):
        if low < high:
            pivot = self._partition(data, low, high)
            self._quick_sort(data, low, pivot - 1)
            self._quick_sort(data, pivot + 1, high)

    def _partition(self, data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

class InsertionSort(SortStrategy):
    def sort(self, data):
        sorted_data = list(data)
        n = len(sorted_data)
        for i in range(1, n):
            key = sorted_data[i]
            j = i - 1
            while j >= 0 and sorted_data[j] > key:
                sorted_data[j + 1] = sorted_data[j]
                j -= 1
            sorted_data[j + 1] = key
        return sorted_data


class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)


def main():
    data = [6, 9, 3, 8, 2]  
    bubble_sort = BubbleSort()
    quick_sort = QuickSort()
    insertion_sort = InsertionSort()
    sorter = Sorter(bubble_sort)
    sorted_data = sorter.sort(data)
    print("Bubble Sort:", sorted_data)
    sorter = Sorter(quick_sort)
    sorted_data = sorter.sort(data)
    print("Quick Sort:", sorted_data)
    sorter = Sorter(insertion_sort)
    sorted_data = sorter.sort(data)
    print("Insertion Sort:", sorted_data)


if __name__ == "__main__":
    main()
