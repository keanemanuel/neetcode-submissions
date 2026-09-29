class Solution:
    def binarySearch(self, row: List[int], target: int) -> bool:
        lo, hi = 0, len(row)-1
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if target == row[mid]:
                return True
            elif target < row[mid]:
                hi = mid-1
            else:
                lo = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        lo, hi = 0, len(matrix)-1
        while lo <= hi:
            mid = lo + (hi-lo) // 2
            if target in matrix[mid]:
                return self.binarySearch(matrix[mid], target)
            elif target < matrix[mid][0]:
                hi = mid-1
            else:
                lo = mid+1
        return False