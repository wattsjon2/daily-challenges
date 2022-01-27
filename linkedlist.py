from hashlib import new


class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

# new_node = Node(5)

# print(new_node.value)
# print(new_node.next)

class LinkedList:
    def __init__(self):
        self.head = None

# linked_list = LinkedList()

    def pushOn(self, new_value):
        new_node = Node(new_value, self.head)
        self.head = new_node


    def append(self, new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node

        last = self.head

        while last.next:
            last = last.next


my_list = LinkedList()

my_list.pushOn(4)
my_list.pushOn(900)

print(my_list.head.value)
print(my_list.head.next.value)