class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix[0]) * len(matrix) - 1
        while start <= end:
            mid = start + ((end - start) // 2) # 5
            x = mid // len(matrix[0]) # 1
            y = mid % len(matrix[0]) # 1
            if target == matrix[x][y]:
                return True
            elif target < matrix[x][y]:
                end = mid - 1
            elif target > matrix[x][y]:
                start = mid + 1
        return False
