# Browsing History navigation using two stacks

def visit(url, back_stack, forward_stack, current):
    if current is not None:
        back_stack.append(current)
    current = url
    forward_stack.clear()
    return current

def go_back(back_stack, forward_stack, current):
    if not back_stack:
        return current
    forward_stack.append(current)
    current = back_stack.pop()
    return current

def go_forward(back_stack, forward_stack, current):
    if not forward_stack:
        return current
    back_stack.append(current)
    current = forward_stack.pop()
    return current

def show_state(back_stack, forward_stack, current):
    print("Back stack:", back_stack)
    print("Current:", current)
    print("Forward stack:", list(reversed(forward_stack)))

if __name__ == '__main__':
    back = []
    forward = []
    current = None
    while True:
        print("\n1) Visit URL  2) Back  3) Forward  4) Show  5) Quit")
        choice = input("> ").strip()
        if choice == '1':
            url = input("URL: ").strip()
            if url:
                current = visit(url, back, forward, current)
        elif choice == '2':
            current = go_back(back, forward, current)
        elif choice == '3':
            current = go_forward(back, forward, current)
        elif choice == '4':
            show_state(back, forward, current)
        elif choice == '5':
            break
        else:
            print("invalid choice")
