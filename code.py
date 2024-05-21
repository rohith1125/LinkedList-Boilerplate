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
