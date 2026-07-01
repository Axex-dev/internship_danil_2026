row = input()

stack = []
pairs = {
    ")":"(",
    "}":"{",
    "]":"["
}

for ch in row:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if not stack or stack[-1] != pairs[ch]:
            print("no")
            break
        stack.pop()
else:
    print("yes" if not stack else "no")