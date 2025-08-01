LeetCode

# 141. Linked List Cycle

Floyd's Tortoise and Hare 演算法（快慢指標法）

能在 O(n) 時間 / O(1) 空間 下完成的方法。

核心概念：

- 用兩個指標：
  - `slow`：每次走一步。
  - `fast`：每次走兩步。
- 若有環，這兩個指標一定會相遇（因為快的會追上慢的）。
- 若沒有環，`fast` 或 `fast.next` 最終會變成 `null`，loop 結束。

# 268. Missing Number

**核心思想：**
用數學公式計算「理論上的總和」，再減去實際陣列的總和，即為缺失的數字。
