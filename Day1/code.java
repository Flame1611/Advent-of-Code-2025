import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;

public class code {
    public static void main(String[] args) throws IOException {
        Scanner file = new Scanner(Path.of("input.txt"));
        System.out.printf("The password is:\n%d\n", Part1(file));
        file.close();
        file = new Scanner(Path.of("input.txt"));
        System.out.printf("The password is:\n%d\n", Part2(file));
        file.close();
    }

    static int Part1(Scanner file) {
        int position = 50;
        int password = 0;
        while (file.hasNext()) {
            String line = file.nextLine();
            char direction = line.charAt(0);
            int distance = Integer.parseInt(line.substring(1));
            switch (direction) {
                case 'L':
                    position -= distance;
                    break;
                case 'R':
                    position += distance;
                    break;
                default:
                    System.out.println("Invalid initial character: " + direction);
                    break;
            }
            while (position < 0 || position > 99) {
                if (position < 0) {
                    position += 100;
                } else {
                    position -= 100;
                }
            }
            if (position == 0) {
                password++;
            }
        }
        return password;
    }

    static int Part2(Scanner file) {
        int lastPosition = 50;
        int position = 50;
        int password = 0;
        while (file.hasNext()) {
            String line = file.nextLine();
            char direction = line.charAt(0);
            int distance = Integer.parseInt(line.substring(1));
            switch (direction) {
                case 'L':
                    lastPosition = position;
                    position -= distance;
                    break;
                    case 'R':
                    lastPosition = position;
                    position += distance;
                    break;
                default:
                    System.out.println("Invalid initial character: " + direction);
                    break;
            }
            if (position == 0) {
                password++;
            }
            while (position < 0 || position > 99) {
                if (lastPosition != 0) {
                    password++;
                }
                if (position < 0) {
                    lastPosition = position;
                    position += 100;
                } else {
                    lastPosition = position;
                    position -= 100;
                }
            }
        }
        return password;
    }
}