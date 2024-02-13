class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bills = 0
        ten_bills = 0

        n = len(bills)
        for bill in bills:
            if bill==5:
                five_bills+=1
            elif bill==10:
                if five_bills<1:
                    return False
                five_bills-=1
                ten_bills+=1
            elif bill==20:
                if five_bills>0 and ten_bills>0:
                    five_bills-=1
                    ten_bills-=1
                elif five_bills>=3:
                    five_bills-=3
                else:
                    return False

        return True

        