import java.io.File;
import java.io.FileNotFoundException;
import java.util.Hashtable;
import java.util.Scanner;

public class advent {

  public static void main(String[] args) {
    System.out.println(one());
    System.out.println(two());

  }

  private static int one() {
    int num = 0;

    Hashtable<Character, Character> change = new Hashtable<>();
    change.put('X', 'A');
    change.put('Y', 'B');
    change.put('Z', 'C');

    Hashtable<Character, Integer> scores = new Hashtable<>();
    scores.put('A', 1);
    scores.put('B', 2);
    scores.put('C', 3);

    File f = new File("input.txt");
    Scanner scnr = null;
    try {
      scnr = new Scanner(f);
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine();
      char opp = currLine.charAt(0);
      char mine = currLine.charAt(2);
      mine = change.get(mine);

      if (mine == opp) { // draw
        num += 3;
      } else if (mine == 'A' && opp == 'C') { // r vs s win
        num += 6;
      } else if (mine == 'B' && opp == 'A') { // p vs r win
        num += 6;
      } else if (mine == 'C' && opp == 'B') { // s vs r win
        num += 6;
      }

      num += scores.get(mine); // regardless add letter score

    }

    return num;
  }

  private static int two() {
    int num = 0;

    Hashtable<Character, Character> lose = new Hashtable<>();
    lose.put('A', 'C');
    lose.put('B', 'A');
    lose.put('C', 'B');

    Hashtable<Character, Character> win = new Hashtable<>();
    win.put('A', 'B');
    win.put('B', 'C');
    win.put('C', 'A');

    Hashtable<Character, Integer> scores = new Hashtable<>();
    scores.put('A', 1);
    scores.put('B', 2);
    scores.put('C', 3);

    File f = new File("input.txt");
    Scanner scnr = null;
    try {
      scnr = new Scanner(f);
    } catch (FileNotFoundException e) {
      e.printStackTrace();
    }

    while (scnr.hasNextLine()) {
      String currLine = scnr.nextLine();
      char opp = currLine.charAt(0);
      char mine = currLine.charAt(2);

      if (mine == 'Y') { // draw
        num += 3;
        num += scores.get(opp);
      } else if (mine == 'X') { // lose
        num += scores.get(lose.get(opp));
      } else if (mine == 'Z') { // win
        num += 6;
        num += scores.get(win.get(opp));
      }

    }

    return num;
  }
}
