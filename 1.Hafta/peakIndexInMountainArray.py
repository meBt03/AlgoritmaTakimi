#peakIndexInMountainArray
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                return i
            else:
                i +=1
