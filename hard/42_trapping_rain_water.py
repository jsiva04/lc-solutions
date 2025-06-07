class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax = []
        suffixMax = []

        res = 0

        prefixMax.append(height[0])
        suffixMax.append(height[-1])

        for i in range(1, len(height)):
            prefixMax.append(max(max(prefixMax), height[i - 1]))

        i = len(height) - 2
        while i >= 0:
            suffixMax.append(max(max(suffixMax), height[i + 1]))
            i -= 1
        
        for i in range(len(height)):
            vol = min(prefixMax[i], suffixMax[len(suffixMax) - 1 - i]) - height[i]
            if not vol <= 0:
                res += vol
        
        return res