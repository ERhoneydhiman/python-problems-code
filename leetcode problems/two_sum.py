nums = [3,3]
tar = 6
class Solution:
    def sub_array(array, target):
        sub = []
        for index, num in enumerate(array):
            compliment = target - num
            if compliment in array:
                sub.append((index,array.index(compliment)))
            return sub
