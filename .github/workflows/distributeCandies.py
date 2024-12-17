#distributeCandies
class Solution(object):
    def distributeCandies(self, candyType):
        if len(set(candyType)) == len(candyType) / 2:
            return len(set(candyType))
        elif len(set(candyType)) > len(candyType) / 2:
            return len(candyType) / 2
        else:
            return len(set(candyType))
