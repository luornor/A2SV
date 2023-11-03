class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # triangle=[[1]]
        # for i in range(rowIndex):
        #     prev_row=[0]+triangle[-1]+[0]
        #     curr_row=[]
        #     for j in range(len(triangle[-1])+1):
        #         curr_row.append(prev_row[j]+prev_row[j+1])       
        #     triangle.append(curr_row)

        # return triangle[rowIndex]
        #base case 
        if rowIndex==0:
            return [1]
        prev_row=self.getRow(rowIndex-1)
        curr=[1]
        for i in range(len(prev_row)-1):
            curr.append(prev_row[i]+prev_row[i+1])
        curr+=[1]
        
        return curr
        