class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        #we  need a map to keep track of lead votes at each time
        self.lead_vote=[]
        self.times=times
        self.persons=persons
        leading=-1
        vote_count=defaultdict(int) #to keep track of vote counts
        for i in range(len(persons)):
            vote_count[persons[i]]+=1
            if vote_count[persons[i]]>=vote_count[leading]:
                leading=persons[i]
            self.lead_vote.append(leading)
        


    def q(self, t: int) -> int:
        l=0
        r=len(self.persons)-1
        ans=-1
        while l<=r:
            mid=(l+r)//2
            #we are looking for number before upperbound
            #so we eliminate lower bound
            if self.times[mid]==t:
                return self.lead_vote[mid]
            elif self.times[mid]<t:
                ans=max(ans,mid)
                l=mid+1
            else:
                r=mid-1

        return self.lead_vote[ans]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)