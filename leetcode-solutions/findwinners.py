"""
You are given an integer array matches where matches[i] = [winneri, loseri] 
indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:
answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.
Note:
You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
For test case 2
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
"""
def findWinners(matches: list[list[int]]) -> list[list[int]]:
    lossers = {}
    for w,l in matches:
        if l in lossers:
            lossers[l]+=1
        else:
            lossers[l]=1
    print(lossers)
    no_loss = set()
    one_loss = []
    for w,l in matches:
        if w not in lossers:
            no_loss.add(w)
        if lossers[l]==1:
            one_loss.append(l)
    
    ans = [sorted(list(no_loss)),sorted(one_loss)]
    return ans


print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))

