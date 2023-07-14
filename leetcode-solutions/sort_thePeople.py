def sortPeople(names, heights):
        #[180,165,170]
        people = list(zip(names,heights))
                #[(names[i],heights[i]) for i in range(len(heights))]
        # bubble sort implementation
        # for i in range(len(heights)):
        #     for j in range(len(heights)-1):
        #         if people[j][1]<people[j+1][1]:
        #             people[j],people[j+1] = people[j+1],people[j]
                    
        # sorted_names = [item[0] for item in people]

        # return sorted_names


        #selection sort implementation
        #studets.sort(key=lambda x: (costs[x[1]],-x[1])) when cost is the same it will use
        #decreasing number of indexes

        # max_index = 0
        # max_height = people[0][1]
        for i in range(len(heights)):
            # max_height = people[i][1]
            max_index = i
            for j in range(i+1,len(heights)):
                if people[j][1] > people[max_index][1]:
                    # max_height=people[max_index][1]
                    max_index = j
            people[i],people[max_index] = people[max_index],people[i]
                    
        sorted_names = [item[0] for item in people]

        return sorted_names



print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
# print(sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))