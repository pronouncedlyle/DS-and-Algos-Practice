import time

#define node (like the constructor)
class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
# define a linked list (using the definition of node)
class linked_list:
    def __init__(self):
        self.head = node()

#add to a linked list
    def append (self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

#print a linked list
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def display_backwards(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        elems.reverse()
        print(elems)

    def display_backwards2(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.insert(0, cur_node.data)
        print(elems)

# Testing the linked list and associated functions

my_list = linked_list()

for i in range(9):
    my_list.append(i)

my_list.display()

tic = time.perf_counter()
my_list.display_backwards()
toc = time.perf_counter()
print(f"Executed in {toc - tic:0.10f} seconds")

tic = time.perf_counter()
my_list.display_backwards2()
toc = time.perf_counter()
print(f"Executed in {toc - tic:0.10f} seconds")