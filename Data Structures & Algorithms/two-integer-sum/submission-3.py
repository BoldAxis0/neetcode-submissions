class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #im gonna assume the list is sorted?
        #clearly the list has duplicates
        #shit, the index is not sorted
        #fk it, we will sort it first

        bums=nums
        nums = sorted(nums)
        

        for num in nums:
            diff =  target-num
            if diff in nums:
                return sorted([bums.index(num), next(i for i, v in zip(reversed(range(len(bums))), reversed(bums)) if v == diff)])
        

        