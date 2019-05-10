def min_difference_align(u, r, R):
    matrix = [[None for i in range(len(r) + 1)] for j in range(len(u) + 1)]                 # r*u
    matrix[0][0] = 0                                                                        # 1
    for i in range(1, len(r) + 1):                                                          # r
        matrix[0][i] = matrix[0][i - 1] + R['-'][r[i - 1]]                                  # 1
    for i in range(1, len(u) + 1):                                                          # u
        matrix[i][0] = matrix[i - 1][0] + R[u[i - 1]]['-']                                  # 1
    for x in range(1, len(u) + 1):                                                          # u*r
        for y in range(1, len(r) + 1):
            if u[x - 1] == r[y - 1]:                                                        # 1
                matrix[x][y] = matrix[x - 1][y - 1]                                         # 1
            else:
                west = matrix[x][y - 1] + R['-'][r[y - 1]]                                  # 1
                north = matrix[x - 1][y] + R[u[x - 1]]['-']                                 # 1
                northWest = matrix[x - 1][y - 1] + R[u[x - 1]][r[y - 1]]                    # 1
                matrix[x][y] = min(north, west, northWest)                                  # n
    x = len(u)                                                                              # 1
    y = len(r)                                                                              # 1
    while y > 0 or x > 0:                                                                   # n
        if x == 0:                                                                          # 1
            u = u[:x] + '-' + u[x:]                                                         # 1
            y = y - 1                                                                       # 1
            continue
        if y == 0:                                                                          # 1
            r = r[:y] + '-' + r[y:]                                                         # 1
            x = x - 1                                                                       # 1
            continue
        if matrix[x][y] - R[u[x - 1]][r[y - 1]] == matrix[x - 1][y - 1]:                    # 1
            if x > 0:                                                                       # 1
                x = x - 1                                                                   # 1
            if y > 0:                                                                       # 1
                y = y - 1                                                                   # 1
        elif matrix[x][y] - R[u[x - 1]]['-'] == matrix[x - 1][y]:                           # 1
            if x > 0:                                                                       # 1
                x = x - 1                                                                   # 1
            r = r[:y] + '-' + r[y:]                                                         # 1
        elif matrix[x][y] - R['-'][r[y - 1]] == matrix[x][y - 1]:                           # 1
            if y > 0:                                                                       # 1
                y = y - 1                                                                   # 1
            u = u[:x] + '-' + u[x:]                                                         # 1
    x = 0                                                                                   # 1
    for i in range(0, len(u)):                                                              # u
        x = x + R[u[i]][r[i]]                                                               # 1
    return x, u, r




