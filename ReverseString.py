# Reverse input string, stack implementation
def reverse_string(s):
    stack = []
    for ch in s:
        stack.append(ch)
    result = ""
    while stack:
        result += stack.pop()
    return result


if __name__ == "__main__":
    while True:
        s = input("Enter string to reverse: ")
        print("Reversed:", reverse_string(s))
