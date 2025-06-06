class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        l, r = 0, len(nums) - 1

        try:
            while r > l:
                if r - l == 1:
                    if nums[l] == target:
                        return l
                    elif nums[r] == target:
                        return r
                    else:
                        return -1

                mid = (l + r) // 2

                if nums[mid] < target:
                    l = mid
                elif nums[mid] > target:
                    r = mid
                else:
                    return mid
        except:
            return -1