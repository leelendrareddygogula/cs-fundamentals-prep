class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = [0] * 2 * len(nums)
        for i in range(len(nums)):
            l[i] = l[i + len(nums)] = nums[i]
        return l