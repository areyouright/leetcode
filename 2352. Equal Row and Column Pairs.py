# 2352. Equal Row and Column Pairs

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len1 = len(grid)
        row = [0]*len1
        col = [0]*len1
        count = 0
        for i in range(len1):
            for j in range(len1):
                row[i] += grid[i][j]
                col[i] += grid[j][i]
        for i in range(len(row)):
            for j in range(len(col)):
                buf_col = []
                if row[i] == col[j]:
                    buf_row = grid[i][:]
                    for k in range(len1):
                        buf_col.append(grid[k][j])
                    if buf_row == buf_col:
                        count += 1
        return count
    
print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(Solution().equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))