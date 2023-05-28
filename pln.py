def count_unique_points(n):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    positions = set([(0, 0)])
    for i in range(n):
        new_positions = set()
        for pos in positions:
            for d in directions:
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                new_positions.add(new_pos)
        positions = new_positions
    return len(positions)



print(count_unique_points(5))