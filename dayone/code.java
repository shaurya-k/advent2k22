import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class advent {

  public static void main(String[] args) {
    System.out.println(one());
    System.out.println(two());

  }

  private static int one() {
    int holder = 0;
    int num = 0;

    File f = new File("input.txt");
    Scanner scnr = null;
    try {
      scnr = new Scanner(f);
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine();
      if (!currLine.equals("")) {
        holder += Integer.parseInt(currLine);
      } else {
        if (holder > num) {
          num = holder;
        }
        holder = 0;
      }
    }

    return num;
  }

  private static int two() {
    int[] holder = new int[3];
    int num = 0;
    Arrays.fill(holder, 0);
    
    File f = new File("input.txt");
    Scanner scnr = null;
    try {
      scnr = new Scanner(f);
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine();
      if (!currLine.equals("")) {
        num += Integer.parseInt(currLine);
      } else {
        if (num > holder[0]) {
          holder[0] = num;
          Arrays.sort(holder);
        }
        num = 0;
      }
    }

    int sum = 0;
    for (int temp : holder) {
      sum += temp;
    }

    return sum;
  }
}
