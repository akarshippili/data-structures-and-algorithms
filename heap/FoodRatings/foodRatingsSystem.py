class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

        self.foodToIndex = {}
        self.highestRatedIn = {}
        for index, food in enumerate(foods): self.foodToIndex[food] = index
        for index, cuisine in enumerate(cuisines):
            if(cuisine not in self.highestRatedIn):
                self.highestRatedIn[cuisine] = []
                heapify(self.highestRatedIn[cuisine])
                heappush(self.highestRatedIn[cuisine], (-1 * self.ratings[index], self.foods[index]))
            heappush(self.highestRatedIn[cuisine], (-1 * self.ratings[index], self.foods[index]))
        print(self.highestRatedIn)
        

    def changeRating(self, food: str, newRating: int) -> None:
        index = self.foodToIndex[food]
        cuisine = self.cuisines[index]
        self.ratings[index] = newRating
        heappush(self.highestRatedIn[cuisine], (-1 * newRating, food))
        

    def highestRated(self, cuisine: str) -> str:

        while(True):
            rating, food = self.highestRatedIn[cuisine][0]
            
            rating *= -1
            index = self.foodToIndex[food]
            
            if(rating == self.ratings[index]): return food
            heappop(self.highestRatedIn[cuisine])





# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
