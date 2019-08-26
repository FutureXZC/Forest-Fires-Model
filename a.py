import check_ignition as check
import copy

def run_model(f_grid, h_grid, i_threshold, w_direction, burn_seeds):
    
    f_grid1 = copy.deepcopy(f_grid)
    b_grid = copy.deepcopy(f_grid)
    
    length = len(f_grid)    
    for a in b_grid:
        for b in range(length):
            a[b] = False
    for b in burn_seeds:
        b_grid[b[0]][b[1]] = True
            
    # 其中一个set是用来加减，另一个用来储存        
    burning_coor = burn_seeds
    burning_coor = set(burning_coor) # 这个set用来加减
    t_burning_coor2 = set(burning_coor) # 这个set用来计算一共有多少个被点燃点
    
    up = True  
    while up:
        for a in range(len(f_grid)):
            for b in range(len(b_grid[a])):
                # 如果这个点是初始的起火点                                       
                if (a,b) in burning_coor:
                    f_grid1[a][b] -= 1
                    # 如果这个点没有燃料量，说明这个点燃烧不了
                    if f_grid1[a][b] == 0:
                        b_grid[a][b] = False
                        burning_coor.remove((a,b))   
                    continue

                # 如果这个点不是初始的起火点，并且此点会因为初始起火点而起火的话 
                if check.check_ignition(b_grid, f_grid1, h_grid, i_threshold,w_direction, a, b) == True:                                                  
                    b_grid[a][b] = True
                    f_grid1[a][b] -= 1
                    burning_coor.add((a,b))
                    t_burning_coor2.add((a,b))
        if (len(burning_coor) == 0):
            up = False
                        
                                        
                   
    initial_burn_area = 0
    final_burn_area = len(t_burning_coor2)
    
    return f_grid1, final_burn_area-initial_burn_area

if __name__ == '__main__':
    print(run_model([[2, 2], [2, 2]], [[1, 1], [1, 1]], 1, 'N', [(0, 0)]))
    print(run_model([[2, 0], [0, 2]], [[1, 1], [1, 1]], 2, 'S', [(0, 0)]))