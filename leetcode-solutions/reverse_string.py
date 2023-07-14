s = ["h","e","l","l","o"]

start = 0
end = len(s)-1
while start<end:
    s[start],s[end]=s[end],s[start]
    end-=1
    start+=1
    

print(s)