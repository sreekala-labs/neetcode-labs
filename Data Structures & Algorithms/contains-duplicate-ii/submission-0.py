class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]!=nums[j]:
                j-=1
            elif nums[i]==nums[j] and abs(i-j)>k:
                i+=1
            elif nums[i]==nums[j] and abs(i-j)<=k:
                return True
        return False