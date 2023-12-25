class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        #build graph that maps ingredient to recipi
        graph = defaultdict(list)
        count = defaultdict(int)
        #how many ingredients does a recipie need
        for recipe,ingredient in zip(recipes,ingredients):
            count[recipe]=len(ingredient)
            for item in ingredient:
                graph[item].append(recipe)

        queue = deque(supplies)
        # print(count)
        # print(graph)
        

        res = []
        while queue:
            supply = queue.popleft()

            #if we can create a recipe
            if supply in recipes:
                res.append(supply)

            for recipe in graph[supply]:
                count[recipe]-=1
                if count[recipe]==0:
                    queue.append(recipe)

        return res




        

        
