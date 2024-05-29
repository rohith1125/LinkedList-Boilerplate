class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

    def create_linked_list(self, values):
        if not values:
            return
        self.head = ListNode(values[0])
        current = self.head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

    def unshift(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_in_middle(self, value, position):
        new_node = ListNode(value)
        if position == 0:  # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index_counter = 0
        while current.next:
            if index_counter == position - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            index_counter += 1

        # If the position is beyond the end of the list, insert at the end
        if index_counter == position - 1:
            current.next = new_node

    def delete_first_node(self):
        if self.head:
            self.head = self.head.next

    def delete_from_middle(self, target_value):
        if not self.head:
            return

        if self.head.value == target_value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == target_value:
                current.next = current.next.next
                return
            current = current.next
    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            # a -> b -> c
            next_node = curr.next   # next_node stores the next node
            curr.next = prev        # pointing the value of current node to previous node
            prev = curr             # updating prev pointer to the current node, so that in the next iteration prev points to this node as prev
            curr = next_node        # updating curr pointer to the next node, so that in the next iteration curr points to the next node as curr
        self.head = prev

    def reverse1(self):
        curr = self.head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
    def rm_dupes_from_sorted_LL(self):
        curr = self.head
        while curr and curr.next:
            if curr.value == curr.next.value:
                curr.next = curr.next.next
            else:
                curr = curr.next
    def rm_dupes_unsorted(self):
        curr = self.head
        prev = None
        dic = {}
        while curr:
            if curr.value in dic:
                dic[curr.value] += 1
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                # a -> b -> c -> d
            else:
                dic[curr.value] = 1
                prev = curr
            curr = curr.next
    def findmiddle2(self):
        slow=fast=self.head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow.value
    def findmiddle(self):
        curr = self.head
        count = 0
        dic = {}
        while curr:
            dic[count] = curr.value
            curr = curr.next
            count += 1
        return dic[count//2]
       
    def pop_last_element(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next

        current.next = None

    def search_in_list(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False

    def get_value_at_index(self, target_index):
        current = self.head
        index = 0
        while current:
            if index == target_index:
                return current.value
            current = current.next
            index += 1
        return None  # Return None if the target index is out of range

    def set(self,index,value):
        current = self.head
        ind_counter = 0
        while current:
            if ind_counter == index:
                current.value = value
                return
            current = current.next
            ind_counter += 1
        print("Index out of bounds")

    def insert(self,value,position):
        index_counter = 0
        current = self.head
        new_node = ListNode(value)
        if position == 0:
            # Insert at the beginning
            new_node.next = self.head
            self.head = new_node
            return

        while current.next:
            current = current.next
        current.next = new_node

        while current:
            if index_counter == position - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            index_counter+=1
# Example usage
values = [1, 2, 3, 4]
ll = LinkedList()
ll.create_linked_list(values)

print("Original list:")
ll.print_linked_list()

# Unshift (insert at the beginning)
ll.unshift(0)
print("List after unshifting 0:")
ll.print_linked_list()

# Insert in the middle
ll.insert_in_middle(5, 2)
print("List after inserting 5 at position 2:")
ll.print_linked_list()

# Delete the first node
ll.delete_first_node()
print("List after deleting the first node:")
ll.print_linked_list()

# Delete a node with a specific value (e.g., 3)
ll.delete_from_middle(3)
print("List after deleting node with value 3:")
ll.print_linked_list()

# Pop the last element
ll.pop_last_element()
print("List after popping the last element:")
ll.print_linked_list()

# Search for a value (e.g., 2)
target_value = 2
found = ll.search_in_list(target_value)
print(f"Value {target_value} found in the list: {found}")

# Get value at a specific index (e.g., index 2)
target_index = 2
value_at_index = ll.get_value_at_index(target_index)
if value_at_index is not None:
    print(f"Value at index {target_index}: {value_at_index}")
else:
    print(f"Index {target_index} is out of range.")

print("\n")
print("LL before manipulation")
ll.print_linked_list()
# Set value at a specific index (e.g., index 1 to value 200)
ll.set(1, 200)
print("List after setting value at index 2 to 9:")
ll.print_linked_list()

# Attempt to set value at an out-of-range index
ll.set(10, 99)
print("List after attempting to set value at out-of-range index 10:")
ll.print_linked_list()


'''

ll = LinkedList()
ll.head = ListNode(1)
ll.head.next = ListNode(2)
ll.head.next.next = ListNode(3)

print("Original list:")
ll.print_linked_list()

ll.reverse()

print("Reversed list:")
ll.print_linked_list()

'''