import sys
import threading
def main():

    def dfs(a, b, seq):
        if a == b:
            return True, seq

        if a > b:
            return False, []

        found, list = dfs(a * 10 + 1, b, seq + [a* 10 + 1])
        if found:
            return True, list

        found, list = dfs(a * 2, b, seq + [a* 2])
        if found:
            return True, list

        return False, []


    a, b = map(int, input().split())
    found, seq = dfs(a, b, [a])

    if found:
        print("YES")
        print(len(seq))
        print(*seq)
    else:
        print("NO")

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()