def main():
    with open("input.txt","r") as f:
        print(f"Answer for Part 1:\n{part1(f)}") 
    with open("input.txt","r") as f:
        print(f"Answer for Part 2:\n{part2(f)}") 

def part1(f:list[str]):
    total = 0
    for line in f:
        ranges = line.split(",")
    ranges = [range_bounds.split("-") for range_bounds in ranges]
    for range_bounds in ranges:
        for number in range(int(range_bounds[0]),int(range_bounds[1])+1):
            number = str(number)
            if number[:int(len(number)/2)] == number[int(len(number)/2):]:
                total += int(number)
    return total

def part2(f):
    total = 0
    for line in f:
        ranges = line.split(",")
    ranges = [range_bounds.split("-") for range_bounds in ranges]
    for range_bounds in ranges:
        for number in range(int(range_bounds[0]),int(range_bounds[1])+1):
            number = str(number)
            midpoint = int(len(number)/2)
            for cutoff in range(midpoint,0,-1):
                if number[cutoff:] == number[:cutoff]:
                    total += int(number)
                    break
    return total

main()