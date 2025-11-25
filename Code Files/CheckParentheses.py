# Check if parentheses are balanced, stack implementation
def is_balanced(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    while True:
        expr = input("Enter any expression to see if the parentheses are balanced: ")
        print("Balanced" if is_balanced(expr) else "Not Balanced")
