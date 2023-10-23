from collections import deque

def solution(priorities, location):
    ans = 0
    q = deque([(p, idx) for idx, p in enumerate(priorities)])
    while q:
        current = q.popleft()
        if any(current[0] < doc[0] for doc in q):
            q.append(current)
        else:
            ans += 1
            if current[1] == location:
                return ans

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))
    priorities = [1, 1, 9, 2, 3, 4]
    location = 1
    print(solution(priorities, location))
    priorities = [1, 1, 2, 1, 1, 1]
    location = 0
    print(solution(priorities, location))