class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # BS col 0, BS the proper row
        m = matrix
        l, r  = 0, len(m) - 1
        row = -1
        # column search to find the row to target
        while row == -1 and l <= r:
            mi = l + (r-l) // 2
            if m[mi][0] == target:
                return True
            elif m[mi][0] < target:
                # move right
                if mi == len(m) - 1:
                    row = mi
                elif m[mi+1][0] > target:
                    row = mi
                else:
                    l = mi + 1
            else:
                if mi == 0:
                    row = mi
                elif m[mi-1][0] < target:
                    row = mi - 1
                else: 
                    r = mi - 1
                
        print(row)
        
        # search within row
        l, r = 0, len(m[0]) - 1
        while l <= r:
            mi = l + (r-l) // 2
            if m[row][mi] == target:
                return True
            if m[row][mi] < target:
                l = mi + 1
            else:
                r = mi - 1
        return False

