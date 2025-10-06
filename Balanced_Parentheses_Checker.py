def is_balanced(expr):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for ch in expr:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping.keys():
            if not stack or mapping[ch] != stack.pop():
                return False
    return not stack

expr = input("Enter expression: ")
print("Balanced" if is_balanced(expr) else "Not Balanced")
