def move1(current, d):
    """
    1 2 3
    4 5 6
    7 8 9
    """
    if d == "U":
        if current <= 3:
            return current
        return current - 3
    if d == "D":
        if current >= 7:
            return current
        return current + 3
    if d == "L":
        if current in [1, 4, 7]:
            return current
        return current - 1
    if d == "R":
        if current in [3, 6, 9]:
            return current
        return current + 1


def move2(current, d):
    """
        1
      2 3 4
    5 6 7 8 9
      A B C
        D
    """
    if ((d == "U" and current in [5, 2, 1, 4, 9]) or (d == "D" and current in [5, 10, 13, 12, 9]) or
            (d == "L" and current in [1, 2, 5, 10, 13]) or (d == "R" and current in [1, 4, 9, 12, 13])):
        return current
    if d == "U":
        if current in [3, 13]:
            return current - 2
        else:
            return current - 4
    if d == "D":
        if current in [1, 11]:
            return current + 2
        else:
            return current + 4
    if d == "L":
        return current - 1
    if d == "R":
        return current + 1

instructions_list = open("data/day02.input").read().splitlines()

code1 = ""
code2 = ""
location1 = 5
location2 = 5
for instructions in instructions_list:
    for i in instructions:
        location1 = move1(location1, i)
        location2 = move2(location2, i)
    code1 += str(location1)
    code2 += f"{location2:X}"

print(f"Solution 1: {code1}")
print(f"Solution 2: {code2}")