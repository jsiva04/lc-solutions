class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]

        if len(nums) == 1:
            return nums[0]

        while r > l:
            mid = (l + r) // 2
            if nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid
            else:
                return nums[mid + 1]