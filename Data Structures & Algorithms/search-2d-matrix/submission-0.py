class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count = len(matrix)
        col_count = len(matrix[0])

        element_count = row_count * col_count

        left = 0
        right = element_count - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // col_count
            c = mid % col_count
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False