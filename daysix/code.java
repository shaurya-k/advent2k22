import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

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

    int index = 0;
    List<Character> buffer = new ArrayList<>();
    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine().strip();
      for (char ch : currLine.toCharArray()) {
        if (index <= 3) {
          buffer.add(ch);
        } else {
          Set<Character> set = new HashSet<>(buffer);
          if (set.size() == 4) {
            return index;
          } else {
            buffer.remove(0);
            buffer.add(ch);
          }

        }

        index += 1;
      }

    }

    return index;
  }

  private static int two() {
    File f = new File("input.txt");
    Scanner scnr = null;
    try {
      scnr = new Scanner(f);
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    int index = 0;
    List<Character> buffer = new ArrayList<>();
    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine().strip();
      for (char ch : currLine.toCharArray()) {
        if (index <= 13) {
          buffer.add(ch);
        } else {
          Set<Character> set = new HashSet<>(buffer);
          if (set.size() == 14) {
            return index;
          } else {
            buffer.remove(0);
            buffer.add(ch);
          }

        }

        index += 1;
      }

    }

    return index;
  }
}
