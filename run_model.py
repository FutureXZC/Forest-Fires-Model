import check_ignition as check

# 更新燃烧状态数组b_grid
def update_b_grid(b_grid, M, burn_seeds):
    b_grid.clear()
    for row in range(M):
        b_grid.append([])
        for col in range(M):
            b_grid[row].append(False)
    for item in burn_seeds:
        b_grid[item[0]][item[1]] = True

def run_model(f_grid, h_grid, i_threshold, w_direction, burn_seeds):
    
    # 是否存在某一格子在燃烧的标记
    is_burning = True

    # 初始化燃烧状态的布尔数组b_grid、M、记录单元格是否燃烧过的布尔数组have_burned、燃烧的单元格数n
    b_grid = []
    M = len(f_grid[0])
    update_b_grid(b_grid, M, burn_seeds)
    have_burned = []
    update_b_grid(have_burned, M, burn_seeds)
    n = len(burn_seeds)
    
    # 记录t+1时刻将燃烧的单元格
    will_burn = []

    # t时刻燃烧时，判定t+1时刻燃烧状态
    while (is_burning):
        for row in range(M):
            for col in range(M):
                if (b_grid[row][col]):
                    f_grid[row][col] -= 1
                    if (f_grid[row][col] > 0):
                        will_burn.append((row, col))
                    continue
                elif (check.check_ignition(b_grid, f_grid, h_grid, i_threshold, w_direction, row, col)):
                    will_burn.append((row, col))
                    if not (have_burned[row][col]):
                        n += 1
                        have_burned[row][col] == True
        update_b_grid(b_grid, M, will_burn)
        if not (len(will_burn)):
            is_burning = False
        will_burn.clear()
    
    return (f_grid, n)  # 返回终止燃烧时的状态

# end def run_model

if __name__ == '__main__':
    print(run_model([[2, 2], [2, 2]], [[1, 1], [1, 1]], 1, 'N', [(0, 0)]))
    print(run_model([[2, 0], [0, 2]], [[1, 1], [1, 1]], 2, 'S', [(0, 0)]))