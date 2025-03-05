class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for no1 in range(len(nums1)):
            Aynı = False
            büyük= -1
            
            for no2 in range(len(nums2)):
                if nums2[no2] == nums1[no1]:
                    Aynı = True
                
                if Aynı and nums2[no2] > nums1[no1]:
                    büyük = nums2[no2]
                    break
            
            result.append(büyük)

        return result
