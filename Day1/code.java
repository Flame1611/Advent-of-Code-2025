import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;

public class code{
    public static void main(String[] args) throws IOException {
        int position = 50;
        int password = 0;
        Scanner file = new Scanner(Path.of("input.txt"));
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
        System.out.printf("The password is:\n%d", password);
        file.close();
    }
}