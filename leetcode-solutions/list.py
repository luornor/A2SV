if __name__ == '__main__':
    N = int(input())

    ans = []

    def execute(list):
        if list[0]=='print':
            print(ans)
        elif list[0]=='sort':
            ans.sort()
        elif list[0]=='pop':
            ans.pop()
        elif list[0]=='reverse':
            ans.reverse()
        elif list[0]=='insert':
            ans.insert(int(list[1]),int(list[2]))
        elif list[0]=='append' in list:
            ans.append(int(list[1]))
        elif list[0]=='remove':
            ans.remove(int(list[1]))
        return 

            



    for i in range(N):
        command = input().split()
        execute(command)

    

    






