password = 0
position = 50
print(position)
with open("input.txt","r") as f:
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
print(f"The password is : \n{password}")