class UnionFind:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        
    
    def find(self,x):
        if self.parent[x]==x:
            return x
        
        return self.find(self.parent[x])
    
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y

    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = UnionFind(n)
        
        mail_index = {}
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in mail_index:
                    parent_idx = dsu.find(i)
                    dsu.union(parent_idx,mail_index[email])
                mail_index[email]=i

        #index and list of accounts
        merge_account={}
        for email,index in mail_index.items():
            parent = dsu.find(index)
            if parent not in merge_account:
                #start with name
                merge_account[parent] = []

            merge_account[parent].append(email)
                
        # print(merge_account.items())
        res = []
        for index,account in merge_account.items():
            name = [accounts[index][0]]
            account.sort()
            account = name+account
            res.append(account)


        return res