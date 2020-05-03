## Explanation

### Discussion

Used a Python list `found_items` to store the file paths with files containing the target suffix.

Recursively searched through each file and directory to get the target paths.

### Time complexity:

We need to look at every file and directory from our starting directory. So the run-time
increases on the order of O(N).

### Space complexity:

We only store the items with the target suffixes. In the worst case, we have only
files and no directories and every file has the target suffix so we store all the file paths.
This would take O(N) space. The average case would be < O(N). 