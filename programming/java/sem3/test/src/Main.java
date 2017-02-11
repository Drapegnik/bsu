import java.io.*;
import java.net.SocketTimeoutException;
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Created by Drapegnik on 04.12.15.
 */
public class Main {

    public static void main(String[] args) {
        Scanner sc1 = null;
        Scanner sc2 = null;
        PrintWriter wr = null;
        try {
            sc1 = new Scanner(new FileReader("input1.txt"));
            sc2 = new Scanner(new FileReader("input2.txt"));
            wr = new PrintWriter(new File("output.txt"));
            MyContainer<ForestTree> a = new MyContainer<>();

            while (sc1.hasNext())
                a.add(new ForestTree(sc1.next(), sc1.nextInt(), sc1.next(), sc1.nextInt()));

            System.out.print("Forest tree: ");
            a.print();
            System.out.println("min:\t" + a.minimum());
            System.out.println("count of on index[0]:\t" + a.count(a.get(0)));
            System.out.println("search on index [2]:\t" + a.search(a.get(2)));
            System.out.print("not changed! ");
            a.print();
            a.sort(null);
            System.out.print("sorted: ");
            a.print();
            System.out.println("\n--------------------------------------------------------\n");

            MyContainer<FruiteTree> b = new MyContainer<>();

            while (sc2.hasNext())
                b.add(new FruiteTree(sc2.next(), sc2.nextInt(), sc2.next(), sc2.nextInt(), sc2.nextInt()));

            System.out.print("Fruite tree: ");
            b.print();
            System.out.println("min:\t" + b.minimum());
            System.out.println("count of on index[2]:\t" + b.count(b.get(2)));
            System.out.println("search on index [2]:\t" + b.search(b.get(2)));
            System.out.print("not changed! ");
            b.print();


        } catch (FileNotFoundException e) {
            System.out.println(e);
        } catch (InputMismatchException e) {
            System.out.println("Incorrect input data!");
        } catch (MyException e) {
            System.out.println(e);
            return;
        } finally {
            if (sc1 != null)
                sc1.close();
            if (sc2 != null)
                sc2.close();
            if (wr != null)
                wr.close();
        }
    }
}
