# https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/792/

def dfs(y, x, grid, odw, n, m, ruchy):
    odw[y][x] = True
    for ruch in ruchy:
        ny = y + ruch[0]
        nx = x + ruch[1]
        
        if not inRange(ny, nx, n, m):
            continue
        
        if grid[ny][nx] == "0":
            continue
        
        if not odw[ny][nx]:
            dfs(ny, nx, grid, odw, n, m, ruchy)
        
def inRange(ny, nx, n, m):
    return (0 <= ny < n and 0 <= nx < m)

def numIslands(grid):
    ruchy = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
    odw = [[False for _  in range(len(grid[0]))] for _ in range(len(grid))]
    w = 0
    
    for i in range(len(grid)):
        for k in range(len(grid[0])):
            if odw[i][k] == False and grid[i][k] == "1":
                w += 1
                dfs(i, k, grid, odw, len(grid), len(grid[0]), ruchy)
                
    return w

print(numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))