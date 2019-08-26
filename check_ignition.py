def check_ignition(b_grid, f_grid, h_grid, i_threshold, w_direction, i, j):

    # 若无燃料，则不可燃烧，直接返回
    if (f_grid[i][j] == 0):
        return False

    # 初始化该单元格(i, j)的可燃性、M、燃烧值和风向图谱
    is_to_burn = False
    M = len(b_grid[0])
    ignition_factor = 0.0
    wind_map = {
        'N': ( (i-2, j-1), (i-2, j), (i-2, j+1) ),
        'S': ( (i+2, j-1), (i+2, j), (i+2, j+1) ),
        'W': ( (i-1, j-2), (i, j-2), (i+1, j-2) ),
        'E': ( (i-1, j+2), (i, j+2), (i+1, j+2) ),
        'NW': ( (i-2, j-2), (i-2, j-1), (i-1, j-2) ),
        'NE': ( (i-2, j+2), (i-2, j+2), (i-1, j+2) ),
        'SW': ( (i+2, j-2), (i+2, j-1), (i+1, j-2) ),
        'SE': ( (i+2, j+2), (i+2, j+1), (i+1, j+2) )
    }

    # 检查相邻的8格
    for row in range(i-1, i+2):
        if (row < 0 or row >= M):
            continue 
        for col in range(j-1, j+2):
            if (col < 0 or col >= M or b_grid[row][col] == False):
                continue
            if (h_grid[row][col] > h_grid[i][j]):
                ignition_factor += 0.5
            elif (h_grid[row][col] == h_grid[i][j]):
                ignition_factor += 1
            elif (h_grid[row][col] < h_grid[i][j]):
                ignition_factor += 2

    # 检查风向
    if (w_direction in wind_map):
        for grid in wind_map[w_direction]:
            row = grid[0]
            col = grid[1]
            if (row < 0 or row >= M or col < 0 or col >= M):
                continue
            if (h_grid[row][col] > h_grid[i][j]):
                ignition_factor += 0.5
            elif (h_grid[row][col] == h_grid[i][j]):
                ignition_factor += 1
            elif (h_grid[row][col] < h_grid[i][j]):

                ignition_factor += 2
    # 检查燃烧值是否大于燃烧阈值
    if (ignition_factor >= i_threshold):
        is_to_burn = True
    return is_to_burn
    
# end def check_ignition()


if __name__ == '__main__':
    print(check_ignition([[True, False], [False, False]], [[2, 2], [2, 2]], [[1, 1], [1, 1]], 1, 'N', 0, 1))
    print(check_ignition([[True, False], [False, False]], [[2, 0], [2, 2]], [[1, 1], [1, 1]], 1, 'N', 1, 0))
    print(check_ignition([[True, True, False], [False, False, False], [False, False, False]], [[1, 1, 1], [1, 1, 1], [1, 0, 0]], [[2, 2, 1], [2, 3, 1], [1, 1, 1]], 1, None, 0, 2))
    print(check_ignition([[True, True, False], [False, False, False], [False, False, False]], [[1, 1, 1], [1, 1, 1], [1, 0, 0]], [[2, 2, 1], [2, 3, 1], [1, 1, 1]], 2, None, 1, 1))