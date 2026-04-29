# Bubble Sort

泡沫排序（ Bubble Sort ）的 Python 實現。

## 演算法說明

泡沫排序是一種簡單的排序演算法，重複遍歷陣列，比較相鄰兩元素並在順序錯誤時交換位置，每趟遍歷會將最大的元素「冒泡」到最後。

- 時間複雜度：O(n²)
- 空間複雜度：O(1)
- 穩定排序：是

## 安裝

```bash
git clone https://github.com/lori9018/linuxTest_0429.git
cd linuxTest_0429
```

## 使用方式

```python
from bubble_sort.bubble_sort import bubble_sort

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 34, 64, 90]
```

## 執行測試

```bash
python3 bubble_sort/bubble_sort.py
```

## 授權

MIT License