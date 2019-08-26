def str2int(s):
    try:
        value = int(s)
        if value >= 0:
            return int(s)
        else:
            return None
    except ValueError:
        return None


def parse_scenario(filename):
    result = dict()
    m = 0
    with open(filename, 'rt') as f:
        # 读第一行：M must > 0
        line_1st = f.readline()
        m = str2int(line_1st.strip())
        if m is None or m <= 0:
            # print("M {} is Error Value.".format(line_1st))
            return None
        # 读 M*M square数据 f_grid
        f_grid = []
        for i in range(0, m):
            l_f_grid = f.readline().strip()
            f_grid.append([str2int(x) for x in l_f_grid.split(',')])
        # 读h_grid
        h_grid = []
        for i in range(0, m):
            l_h_grid = f.readline().strip()
            h_grid.append([str2int(x) for x in l_h_grid.split(',')])
        # i_threshold, must <= 8
        l_i = f.readline().strip()
        i_threshold = str2int(l_i)
        if i_threshold is None or i_threshold > 8 or i_threshold <= 0:
            # print("i_threshold {} is Error Value.".format(l_i))
            return None
        # w_direction
        w_direction = f.readline().strip()
        # 判断方向是否合法;
        if w_direction not in ['E', 'S', 'W', 'N', 'SE', 'NE','SW', 'NW', '', 'None']:
            # print('w_direction {} is Error Value.'.format(w_direction))
            return None
        # burn_seeds
        burn_seeds = []
        l_bs = f.readlines()
        for l in l_bs:
            seed = tuple([str2int(x) for x in l.strip().split(',')])
            # 超出景观地图范围;
            if seed[0] is None or seed[0] >= m or seed[1] is None or seed[1] >= m:
                # print('burn_seed {} exceed limit.'.format(seed))
                return None
            # 燃料是否大于0;
            load_seed = f_grid[seed[0]][seed[1]]
            if load_seed <= 0:
                # print('burn_seed {} \'s fuel load {} is Not Valid'.format(seed, load_seed))
                return None
            burn_seeds.append(seed)

        result['f_grid'] = f_grid
        result['h_grid'] = h_grid
        result['i_threshold'] = i_threshold
        result['w_direction'] = w_direction
        result['burn_seeds'] = burn_seeds

        return result


if __name__ == '__main__':
    r = parse_scenario('bf0.dat')
    print(r, '\n')
