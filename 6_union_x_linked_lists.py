"""
Union and Intersections linked list

2 linked lists 

Return a linked list of union or intersection
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


"""
A U B

A or B

a -> hash table

Intersection
Cycle through 1st l list
Cycle through 2nd l list
Put 1st ll in hash
See if find 2nd one 
Then add up the ones with 2
Or put the ones with 2 in a 3 llist

Union is A || B 


"""


def union(llist_1, llist_2):
    node_1 = llist_1.head
    node_2 = llist_2.head

    union_map = dict()

    while node_1.next != None:
        value_1 = node_1.value
        if value_1 not in union_map:
            union_map[value_1] = 1
        node_1 = node_1.next

    while node_2.next != None:
        value_2 = node_2.value
        if value_2 not in union_map:
            union_map[value_2] = 1
        node_2 = node_2.next

    return list(union_map.keys())


def intersection(llist_1, llist_2):
    # Your Solution Here
    pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
