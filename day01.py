directions = open("data/day01.input").read()

directions = directions.split(",")


def turn(f, t):
    v = 1 if t == "R" else -1
    return f[1]*v, -f[0]*v


position = (0, 0)
seen_positions = set()
facing = (0, 1)
soln2 = set()
for direction in directions:
    direction = direction.strip()
    facing = turn(facing, direction[0])
    distance = int(direction[1:])
    new_positions = set()
    if len(soln2) == 0:
        for d in range(distance):
            position = position[0] + facing[0], position[1] + facing[1]
            new_positions.add(position)
        soln2 = new_positions.intersection(seen_positions)
        seen_positions = seen_positions.union(new_positions)
    else:
        position = position[0] + facing[0]*distance, position[1] + facing[1]*distance

soln1 = abs(position[0]) + abs(position[1])
soln2 = soln2.pop()
soln2 = abs(soln2[0]) + abs(soln2[1])
print(f"Solution 1: {soln1}")
print(f"Solution 2: {soln2}")

