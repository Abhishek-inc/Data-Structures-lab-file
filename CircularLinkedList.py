# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    def insert_in_middle(self, data, position):
        if position <= 1 or self.head is None:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 1

        while count < position - 1 and temp.next != self.head:
            temp = temp.next
            count += 1

        new_node.next = temp.next
        temp.next = new_node

    def search(self, key):
        if self.head is None:
            return False
        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def delete(self, key):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        prev = None

        while True:
            if temp.data == key:
                if prev is None:
                    # Deleting head
                    if temp.next == self.head:
                        self.head = None
                        print("Deleted:", key)
                        return
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = temp.next
                    last.next = self.head
                else:
                    prev.next = temp.next
                print("Deleted:", key)
                return

            prev = temp
            temp = temp.next
            if temp == self.head:
                break

        print("Value not found.")

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        print("List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

if __name__ == "__main__":
    ll = CircularLinkedList()
    ll.insert_at_end(5)
    ll.insert_at_end(10)
    ll.insert_at_end(15)
    ll.insert_at_end(20)

    while True:
        print("\n--- Circular Linked List Menu ---")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert at a position")
        print("4. Search")
        print("5. Delete by value")
        print("6. Display list")
        print("7. Exit")

        ch = input("> ").strip()

        if ch == '1':
            x = input("Enter value: ")
            ll.insert_at_beginning(x)

        elif ch == '2':
            x = input("Enter value: ")
            ll.insert_at_end(x)

        elif ch == '3':
            x = input("Enter value: ")
            p = int(input("Enter position: "))
            ll.insert_in_middle(x, p)

        elif ch == '4':
            key = input("Search value: ")
            print("Found" if ll.search(key) else "Not found")

        elif ch == '5':
            key = input("Delete which value? ")
            ll.delete(key)

        elif ch == '6':
            ll.display()

        elif ch == '7':
            break

        else:
            print("Invalid choice.")