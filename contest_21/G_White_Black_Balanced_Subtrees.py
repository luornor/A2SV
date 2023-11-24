import sys

def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def read_string():
    return input()

def print_output(value):
    print(value)

def print_output_same_line(value):
    print(value, end=' ')



for _ in range(read_int()):
    n = read_int()
    c = read_int_list()
    b = read_string()
    k = 0
    v = [0]
    f = [0] * (n + 1)
    d = [0] * (n + 1)
    a = [[] for i in range(n + 1)]

    for i in range(n):
        if b[i] == 'W':
            v.append(1)
        else:
            v.append(-1)

    for i in range(n - 1):
        a[i + 2].append(c[i])
        a[c[i]].append(i + 2)

    s = [1]
    
    while s:
        z = s[-1]

        if not f[z]:
            f[z] = 1
            for i in a[z]:
                if not f[i]:
                    s.append(i)
        else:
            s.pop()
            total_sum = v[z]

            for i in a[z]:
                total_sum += d[i]

            if not total_sum:
                k += 1

            d[z] = total_sum

    print_output(k)
