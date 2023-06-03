if __name__ == '__main__':
    N = int(input())

    def insert_item(list,x,y):
        return list.insert(x,y)

    def execute(list):
        if 'print' in list:
            print(list)
        elif 'sort' in list:
            list.sort()
        elif 'pop' in list:
            list.pop()
        elif 'reverse' in list:
            list.reverse()
        elif ''

            



    for i in range(N):
        command = input().split()
        execute(command)

    






