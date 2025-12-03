import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;

public class code{
    public static void main(String[] args) throws IOException {
        Scanner file = new Scanner(Path.of("input.txt"));
        System.out.printf("The answer to part 1 is:\n%d\n",part1(file));
        file = new Scanner(Path.of("input.txt"));
        System.out.printf("The answer to part 2 is:\n%d\n",part2(file));
        file.close();
    }

    static int part1 (Scanner file) {
        return 0;
    }
    static int part2 (Scanner file) {
        return 0;
    }
}