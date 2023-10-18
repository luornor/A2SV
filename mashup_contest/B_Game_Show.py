def solve(coins,n,prices):
    # prices.sort()
    max_prize=max(prices)
    max_prices=0
    for m in range(2,max_prize+1):
        count=0
        k=coins
        for price in prices:
            if price%m==0:
                count+=1
            elif k>=price:
                k-=price
                count+=1
            else:
                break

        max_prices=max(max_prices,count)


    print(max_prices)
    

    


k,n=map(int,input().split())
prices=list(map(int,input().split()))
solve(k,n,prices)