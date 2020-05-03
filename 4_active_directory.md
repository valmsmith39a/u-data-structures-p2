## Explanation

### Discussion
2 lists in Group class were part of problem definition.
One list used to store groups, the other list used to store users.

### Time complexity
The is_user_in_group function traverses through each element in a group
which can be a group or a user. In the worst case, we have to search 
through all the elements in all the parent and children groups, for a 
run-time of O(N). The average case would be < O(N) time.

### Space complexity
In the worst case we need to store all the elements of the parent/child groups
resulting in space increasing on the order of O(N). The aveage case would be 
< O(N) space.
