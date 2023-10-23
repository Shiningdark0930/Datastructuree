from collections import deque

def solution(pr):
    n = len(pr)
    ans = [0] * n

    stack = deque()

    for i in range(n):
        while stack and pr[i] < pr[stack[-1]]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    for i in stack:
        ans[i] = n - 1 - i

    return ans

if __name__ == "__main__":
    pr = [1000, 2000, 3000, 2000, 3000]
    result = solution(pr)
    print(result)