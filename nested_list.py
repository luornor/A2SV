if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    print(max(records))
    for i in range(len(records)):
        max_score=records[i][1]
        for item in records[i]:
            if item>max_score:
                max_score=item
