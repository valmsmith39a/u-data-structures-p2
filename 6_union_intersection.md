## Explanation

### Discussion 

Linked lists were used because they were part of the problem definition.

Dictionaries used to create maps to efficiently track and 
lookup values in a list or values common to both lists. 

### Time complexity

In both union and intersection functions, 2 while loops were used, for a run-time of 2*O(N), which can be simplified to O(N) or linear time.

Looking up values using a dictionary takes an average of O(1) or constant time. O(N) + O(1) => O(N) time

### Space complexity

Union:
In the worst case, every value in each list are unique and we have to store every value. Memory space required would increase 
on the order of O(N). The average case would be < O(N) space.

Intersection:
In the worst case, list values are unique and list 1 and list 2 are identical. The intersection_list would need to store all the values, so O(a) + O(b) or simplified to O(N) space. The map_1 dictionary would need to store all the values of one of the lists. The average space complexity would 
be < O(N)
