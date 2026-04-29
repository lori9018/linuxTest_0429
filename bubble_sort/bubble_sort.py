"""
Bubble Sort 泡沫排序算法

原理：
重複遍歷陣列，比較相鄰兩元素若順序錯誤則交換位置，
每趟遍歷會將最大的元素「冒泡」到最後。

時間複雜度：O(n²)
空間複雜度：O(1)
穩定排序：是
"""


def bubble_sort(arr):
    """
    對輸入的陣列進行泡沫排序（原地排序）。

    參數：
        arr: 要排序的可變順序列表

    回傳：
        排序後的陣列（會修改原陣列）
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", data)
    print("Sorted:", bubble_sort(data))
