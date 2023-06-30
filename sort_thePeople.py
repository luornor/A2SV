def sortPeople(names, heights):
        #[180,165,170]
        people = [(names[i],heights[i]) for i in range(len(heights))]
        
        for i in range(len(heights)):
            for j in range(len(heights)-1):
                if people[j][1]<people[j+1][1]:
                    people[j],people[j+1] = people[j+1],people[j]
                    
        sorted_names = [item[0] for item in people]

        return sorted_names