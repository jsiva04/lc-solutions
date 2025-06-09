class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 1
        l, r = 0, 1

        while l < len(s):
            hmap = {}
            hmap[s[l]] = 0

            while r < len(s) and s[r] not in hmap:
                hmap[s[r]] = 0
                r += 1
            
            res = max(res, r - l)
            l += 1
            r = l + 1
        
        return res