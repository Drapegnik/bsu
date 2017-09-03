import java.io.FileNotFoundException;
import java.io.File;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Created by Drapegnik on 12.12.16.
 */
public class Parser {

    private static String regexpToRemove = ">\\s*</\\w+>";
    private static String fileName = "input.xml";
    private static String xml;

    public static void main(String[] args) {
        (new Parser()).doParsing();
    }

    private void readFile(String fileName) {
        try {
            Scanner scanner = new Scanner(new File(fileName));
            StringBuilder stringBuilder = new StringBuilder();

            while (scanner.hasNextLine()) {
                stringBuilder.append(scanner.nextLine());
                stringBuilder.append("\n");
            }

            xml = stringBuilder.toString();
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println(e.getClass() + ": " + e.getMessage());
        }
    }

    private void doParsing() {
        readFile(fileName);
        System.out.println(xml);

        Pattern r = Pattern.compile(regexpToRemove, Pattern.MULTILINE);
        Matcher m = r.matcher(xml);

        if (m.find())
            System.out.println(m.replaceAll("/>"));
    }
}
