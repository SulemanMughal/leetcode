## Big-O Comparison Cheatsheet

This section visualizes common time complexity classes to compare their growth as n increases.

### Mermaid chart (renders in GitHub/VS Code)

```mermaid
%% Compare growth for n = 1..10
xychart-beta
    title "Growth of common complexities"
    x-axis "n" 1 --> 10
    y-axis "f(n)" 0 --> 3700000

    line "O(1)" [1,1,1,1,1,1,1,1,1,1]
    line "O(log n)" [0,1,1,2,2,2,2,3,3,3]
    line "O(n)" [1,2,3,4,5,6,7,8,9,10]
    line "O(n log n)" [0,2,5,8,12,16,19,24,28,33]
    line "O(n^2)" [1,4,9,16,25,36,49,64,81,100]
    line "O(2^n)" [2,4,8,16,32,64,128,256,512,1024]
    line "O(n!)" [1,2,6,24,120,720,5040,40320,362880,3628800]

```

Notes:
- Values are illustrative (rounded) for comparison; constants are ignored in Big-O.
- y-axis uses raw values to show separation; O(n!) explodes rapidly.

### Quick reference

- O(1): Hash table access, push/pop on stack
- O(log n): Binary search, balanced BST operations
- O(n): Linear scan, finding max/min
- O(n log n): Efficient sorts (merge/quick average), heap operations over n items
- O(n^2): Bubble/selection/insertion sort (worst/avg), pairwise comparisons
- O(2^n): Brute-force subsets, naive recursion for Fibonacci
- O(n!): Traveling Salesman brute-force permutations

### PNG chart (optional)

If your platform doesn’t render Mermaid, you can generate a PNG via a small Python script (see `scripts/big_o_chart.py`) and view it at `assets/big_o_growth.png`.

Generate locally:

1) Ensure Python 3 is available and install matplotlib
2) Run the script to create the image

Commands (macOS, zsh):

```bash
python3 -m pip install --user matplotlib
python3 scripts/big_o_chart.py
open assets/big_o_growth.png
```

Embedded image (will appear after you generate it):

![Big-O growth](assets/big_o_growth.png)
