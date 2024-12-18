class Solution(object):
    def containsDuplicate(self, nums):
        kontrol = 0
        for i in nums:
            sayac = 0
            for j in nums:
                if i == j:
                    sayac = sayac + 1
            if sayac > 1:
                kontrol = 1       
        if kontrol == 0:
            return False
        else:
            return True
