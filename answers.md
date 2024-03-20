# CMPS 2200 Reciation 5
## Answers

**Name:**Benjamin Horowitz


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**  
**How do the running times compare to the asymptotic bounds? **

Quicksort works in nlogn time, which is consistent with the results we got. Timsort also works is nlogn time, but according to the python documentation it is optimized for real world data, which may explain its good performance for the unsorted array case. 




- **1c.** 
**How does changing the type of input list change the relative performance of these algorithms? **
Quicksort with the fixed low pivot performs very poorly for sorted arrays, as it bins every number into 1 bucket (as they will all be greater than the pivot), which reduces the time complexity to O(n^2).
