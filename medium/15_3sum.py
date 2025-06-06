class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < len(nums) and l > i and r > l:
                if (nums[l] + nums[r]) < target:
                    l += 1
                elif (nums[l] + nums[r]) > target:
                    r -= 1
                else:
                    ans = sorted([nums[i], nums[l], nums[r]])
                    if ans not in res:
                        res.append(ans)
                    l += 1
                    r -= 1
        return res