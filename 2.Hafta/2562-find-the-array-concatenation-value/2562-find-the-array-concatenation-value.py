class Solution(object):
    def findTheArrayConcVal(self, nums):
        l, r = 0, len(nums) - 1
        result = 0
        while l <= r: 
            if l == r: #Eğer l == r, tek bir eleman kaldığında onu kendisiyle birleştiriyoruz
                result += nums[l]
            else:
                result += int(str(nums[l]) + str(nums[r]))  #İki sayıyı birleştir
            l += 1
            r -= 1
        return result
