from collections import deque


def solve():
    n,m = map(int,input().split())
    queue = deque()

    max_val = max(n, m) * 2 + 1
    queue.append((n,0))
    visited = set()
    visited.add(n)
    while queue:
        num,count = queue.popleft()
        if num==m:
            return count

        next_numbers = [num*2, num - 1]

        for next_num in next_numbers:
            if next_num> max_val:
                continue
            if next_num > 0 and next_num not in visited:
                queue.append((next_num, count + 1))
                visited.add(next_num)

print(solve())

