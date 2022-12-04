import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class advent {

  public static void main(String[] args) {
    System.out.println(one());
    System.out.println(two());

  }

  private static int one() {
    File f = new File("input.txt");
    Scanner scnr = null;
    try {
      scnr = new Scanner(f);
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    int total = 0;

    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine().strip();
      String[] parts = currLine.split(",");
      String[] firstRange = parts[0].split("-");
      int one = Integer.parseInt(firstRange[0]);
      int two = Integer.parseInt(firstRange[1]);
      String[] secondRange = parts[1].split("-");
      int three = Integer.parseInt(secondRange[0]);
      int four = Integer.parseInt(secondRange[1]);

      if ((one <= three && two >= four) || (three <= one && four >= two))
        total += 1;

    }

    return total;
  }

  private static int two() {
    File f = new File("input.txt");
    Scanner scnr = null;
    try {
      scnr = new Scanner(f);
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    int total = 0;

    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine().strip();
      String[] parts = currLine.split(",");
      String[] firstRange = parts[0].split("-");
      int one = Integer.parseInt(firstRange[0]);
      int two = Integer.parseInt(firstRange[1]);
      String[] secondRange = parts[1].split("-");
      int three = Integer.parseInt(secondRange[0]);
      int four = Integer.parseInt(secondRange[1]);
      int min = Math.max(one,three);
      int max = Math.min(two,four);
      
      if(max - min >= 0)
        total += 1;

    }

    return total;
  }
}
