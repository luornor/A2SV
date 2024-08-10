a,b,c,d = map(int,input().split())
Misha = (a,c)

Vasya = (b,d)

m_p = max((3*a)//10,a-(a*c)//250)

v_p =  max((3*b)//10,b-(b*d)//250)

if m_p>v_p:
    print('Misha')
elif m_p==v_p:
    print('Tie')
else:
    print('Vasya')