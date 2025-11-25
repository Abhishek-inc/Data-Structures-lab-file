# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty.")
            return
        print("Deleting:", self.head.data)
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.next is None:
            print("Deleting:", self.head.data)
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        print("Deleting:", temp.next.data)
        temp.next = None

    def insert_after(self, value, new_value):
        temp = self.head
        while temp:
            if temp.data == value:
                new_node = Node(new_value)
                new_node.next = temp.next
                temp.next = new_node
                print(f"Inserted {new_value} after {value}")
                return
            temp = temp.next
        print("Value not found.")

    def delete_after(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.next:
                    print(f"Deleting: {temp.next.data}")
                    temp.next = temp.next.next
                else:
                    print("No node exists after the given value.")
                return
            temp = temp.next
        print("Value not found.")

    def display(self):
        temp = self.head
        print("List:", end=" ")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(15)
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(25)

    while True:
        print("\n--- Linked List Menu ---")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Insert after value")
        print("4. Delete at beginning")
        print("5. Delete at end")
        print("6. Delete after value")
        print("7. Display list")
        print("8. Exit")

        ch = input("> ").strip()

        if ch == '1':
            x = input("Enter value: ")
            ll.insert_at_beginning(x)

        elif ch == '2':
            x = input("Enter value: ")
            ll.insert_at_end(x)

        elif ch == '3':
            v = input("Insert after which value? ")
            x = input("Enter new value: ")
            ll.insert_after(v, x)

        elif ch == '4':
            ll.delete_at_beginning()

        elif ch == '5':
            ll.delete_at_end()

        elif ch == '6':
            v = input("Delete after which value? ")
            ll.delete_after(v)

        elif ch == '7':
            ll.display()

        elif ch == '8':
            break

        else:
            print("Invalid choice.")
