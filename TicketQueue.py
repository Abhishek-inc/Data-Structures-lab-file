# Ticketing System using linear queue
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def show(self):
        return self.items


if __name__ == '__main__':
    q = Queue()
    counter = 1

    while True:
        print("\n1) Generate Ticket  2) Serve Ticket  3) Show Queue  4) Quit")
        choice = input("> ").strip()

        if choice == '1':
            ticket = f"T{counter}"
            q.enqueue(ticket)
            print("Generated:", ticket)
            counter += 1

        elif choice == '2':
            served = q.dequeue()
            if served:
                print("Served:", served)
            else:
                print("No tickets to serve")

        elif choice == '3':
            print("Queue:", q.show())

        elif choice == '4':
            break

        else:
            print("invalid choice")
