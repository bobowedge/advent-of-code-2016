def is_triangle(triangle):
    triangle.sort()
    a, b, c = triangle
    return a + b > c


def soln1(triangles):
    possibles = 0
    for triangle in triangles:
        triangle = [int(x) for x in triangle.split()]
        if is_triangle(triangle):
            possibles += 1
    return possibles


def soln2(triangles):
    possibles = 0
    for i in range(0, len(triangles), 3):
        row0 = [int(x) for x in triangles[i].split()]
        row1 = [int(x) for x in triangles[i+1].split()]
        row2 = [int(x) for x in triangles[i+2].split()]
        triangle1 = [row0[0], row1[0], row2[0]]
        triangle2 = [row0[1], row1[1], row2[1]]
        triangle3 = [row0[2], row1[2], row2[2]]
        if is_triangle(triangle1):
            possibles += 1
        if is_triangle(triangle2):
            possibles += 1
        if is_triangle(triangle3):
            possibles += 1
    return possibles


triangles = open("data/day03.input").read().splitlines()
print(f"Solution 1: {soln1(triangles)}")
print(f"Solution 2: {soln2(triangles)}")
