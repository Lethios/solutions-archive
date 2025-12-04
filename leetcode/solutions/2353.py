# https://leetcode.com/problems/design-a-food-rating-system/

from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_dict = {}
        self.sort_cuisine = defaultdict(SortedList)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_dict[food] = (cuisine, rating)
            self.sort_cuisine[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, old_rating = self.food_dict[food]

        self.food_dict[food] = (cuisine, newRating)

        self.sort_cuisine[cuisine].discard((-old_rating, food))
        self.sort_cuisine[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.sort_cuisine[cuisine][0][1]
