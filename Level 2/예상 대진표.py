def solution(n, a, b):
    arr = list(range(n))
    a -= 1
    b -= 1
    a, b = min(a, b), max(a, b)
    ans = 1

    while True:
        temp = []
        for i in range(len(arr) // 2):
            if (arr[i * 2], arr[i * 2 + 1]) == (a, b):
                return ans

            if arr[i * 2 + 1] in (a, b):
                temp.append(arr[i * 2 + 1])
            else:
                temp.append(arr[i * 2])

        arr = temp
        ans += 1