def solution(s):
    stack = []
    
    for c in s:
        stack.append(c)
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    
    return int(stack == [])