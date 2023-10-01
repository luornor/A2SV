n, k = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
max_len = 0
seg_l, seg_r = 0, 0
hmap = {}
#sliding window
#a window of k elements 
while r < n:
    if arr[r] in hmap:
        hmap[arr[r]] += 1
    else:
        hmap[arr[r]] = 1
    r += 1
    while len(hmap) > k:
        hmap[arr[l]] -= 1
        if hmap[arr[l]] == 0:
            del hmap[arr[l]]
        l += 1

    if max_len < r - l:
        seg_l, seg_r = l + 1, r
        max_len = r - l

print(seg_l, seg_r)
