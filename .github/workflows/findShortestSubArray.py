#findShortestSubArray
class Solution(object):
    def findShortestSubArray(self, nums):
        frequency = {}
        first_index = {}
        last_index = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in frequency:
                frequency[num] = 0
                first_index[num] = i
            frequency[num] += 1
            last_index[num] = i

        degree = max(frequency.values())

        min_length = len(nums)
        for num, freq in frequency.items():
            if freq == degree:
                length = last_index[num] - first_index[num] + 1
                min_length = min(min_length, length)
        return min_length
