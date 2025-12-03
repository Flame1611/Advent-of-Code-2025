def main():
    with open("input.txt","r") as f:
        print(f"The password is : \n{Part1(f)}")
    with open("test.txt","r") as f:
        print(f"The password is : \n{Part2(f)}")

def Part1(f: list[str]) -> int:
    password = 0
    position = 50
    for line in f:
        direction, distance = line[0], int(line[1:])
        match direction.upper():
            case "L":
                position -= distance
            case "R":
                position += distance
        while position < 0 or position > 99:
            if position < 0:
                position += 100
            else:
                position -= 100
        if position == 0:
            password += 1
    return password

def Part2(f: list[str]) -> int:
    password = 0
    position = 50
    last_position = 50
    for line in f: # type: ignore
        direction, distance = line[0], int(line[1:])
        match direction.upper():
            case "L":
                last_position = position
                position -= distance
            case "R":
                last_position = position
                position += distance
        if position == 0:
            password += 1
        while position < 0 or position > 99:
            if last_position != 0:
                password += 1
            if position < 0:
                position += 100
            else:
                position -= 100
    return password

main()