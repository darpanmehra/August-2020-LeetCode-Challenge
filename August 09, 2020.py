'''
994. Rotting Oranges

In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        columns = len(grid[0])
        rotten = deque()
        fresh = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        time_elapsed = 0
        while rotten and fresh > 0:
            time_elapsed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x+di, y+dj
                    if xx < 0 or yy < 0 or xx >= rows or yy >= columns:
                        continue
                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue
                    fresh -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx, yy))
        return time_elapsed if fresh == 0 else -1
