def main():
    with open("input.txt","r") as f:
        print(f"Answer for Part 1:\n{part2(f,2)}") 
    with open("input.txt","r") as f:
        print(f"Answer for Part 1:\n{part2(f)}") 

def part1(f):
    total = 0
    for line in f:
        line = line.strip()
        max = "!"
        second_max = "!"
        for number in range(len(line)-1):
            if max < line[number]:
                max = line[number]
                second_max = line[number+1]
            elif second_max < line[number]:
                second_max = line[number]
        if second_max < line[number+1]:
                second_max = line[number+1]
        total += int(max + second_max)
    return total

def part2(f, battery_size = 12): # Attempting to make it scalable for any battery sized 2+, but it only def works on size 2 for now
    total = 0
    for line in f:
        line = line.strip()
        battery = ["!"]*battery_size
        # for digits_left in range(battery_size-1,-1,-1):
        for number in range(len(line)-(battery_size-1)):
            for i in range(battery_size):
                if line[number] > battery[i]:
                    battery[i] = line[number]
                    for j in range(1,battery_size-(i)):
                        battery[i+j] = line[number+i+j]
                    break
        for ending in range(battery_size-1,0,-1):
            if battery[-ending] < line[-ending]:
                battery[-ending:] = line[-ending:]
                break
        voltage = ""
        for digit in battery:
            voltage += digit
        total += int(voltage)
    return total

main()