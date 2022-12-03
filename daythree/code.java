import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
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
      String one = currLine.substring(0, currLine.length() / 2);
      String two = currLine.substring(currLine.length() / 2, currLine.length());
      Map<Character, Integer> map = new HashMap<>();
      for (char uno : one.toCharArray()) {
        map.put(uno, 1); // just to check if there, count doesn't matter
      }
      char common = '}';
      for (char dos : two.toCharArray()) {
        if (map.get(dos) != null) {
          common = dos;
          break;
        }
      }

      if (Character.isLowerCase(common)) {
        total += common - 96; // 'a' - 96 = 1
      } else {
        total += common - 38; // 'A' - 38 = 27
      }

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
    int iter = 1;
    String first = "";
    String second = "";
    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine().strip();
      if (iter == 1) {
        first = currLine;
        iter += 1;
      } else if (iter == 2) {
        second = currLine;
        iter += 1;
      } else if (iter == 3) {
        String third = currLine;
        char common = '}';

        Map<Character, Integer> map = new HashMap<>();
        for (char uno : first.toCharArray()) {
          map.put(uno, 1); // mapping all to 1 regardless
        }
        for (char dos : second.toCharArray()) {
          if (map.get(dos) != null && map.get(dos) != 2) {
            map.put(dos, 2); // only to 2, if exists in prev loop
          }
        }
        for (char tres : third.toCharArray()) {
          if (map.get(tres) != null && map.get(tres) == 2) {
            common = tres; // if exists in third plus from second and first
            break;
          }
        }

        if (Character.isLowerCase(common)) {
          total += common - 96;
        } else {
          total += common - 38;
        }

        iter = 1;
      }

    }

    return total;
  }
}
