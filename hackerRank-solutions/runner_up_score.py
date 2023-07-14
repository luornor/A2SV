if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(arr)
    n_max = max(arr1)
    
    print(max([item for item in arr1 if item<n_max]))