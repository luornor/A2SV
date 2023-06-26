s = input()

hmap = {}
for ch in s:
    if ch in hmap:
        hmap[ch]+=1
    hmap[ch] = 1

if len(hmap)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')