class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        process_heap = [] #to store tasks based on execution time
        #keep track of original index
        for i,val in enumerate(tasks):
            val.append(i)

        tasks.sort() #sort tasks by arrival time
        current_time = tasks[0][0]
        j = 0
        ans = []
        while j<len(tasks) or process_heap:
            #at each time we  have certain processes in the heap
            while j<len(tasks) and current_time>=tasks[j][0]:
                execution_time = tasks[j][1]
                index = tasks[j][2]
                heappush(process_heap,(execution_time,index))
                j+=1
            #process elements in heap
            if process_heap:
                time,idx= heappop(process_heap)
                current_time+=time
                ans.append(idx)
            else:
                #if there is nothing to process initially
                current_time = tasks[j][0]
        
        return ans

        