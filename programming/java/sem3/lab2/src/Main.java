import java.util.*;
import java.util.Stack;
import java.util.StringTokenizer;

/**
 * Created by Drapegnik on 12.11.15.
 */
public class Main{

    private static Stack <Character> op = new Stack<Character>();
    private static Stack <Integer> num = new Stack<Integer>();
    private static String sPol = "";

    public static int priority (char op) {
        return (op == '+' || op == '-') ? 1 : (op == '*' || op == '/') ? 2 : -1;
    }

    public static void calc (char op) {
        try {
            int r = num.pop();
            int l = num.pop();
            //System.out.println(l+" "+op+" "+r);
            sPol += op + " ";
            switch (op) {
                case '+':  num.push(l + r);  break;
                case '-':  num.push(l - r);  break;
                case '*':  num.push(l * r);  break;
                case '/':  num.push(l / r);  break;
            }
        }catch (EmptyStackException er){
            System.out.println("misses operands!");
            System.exit(1);
        }
    }

    public static void main(String[] args) {
        String s = args[0];
        StringTokenizer st = new StringTokenizer(s, "()+-*/", true);

        while (st.hasMoreTokens()) {
            String token = st.nextToken();
            if (token.equals("("))
                op.push('(');
            else if (token.equals(")")){
                try{
                    while (!op.peek().equals('('))
                        calc(op.pop());
                    op.pop();
                }catch (EmptyStackException er){
                    System.out.println("bad brake notation!");
                    System.exit(1);
                }
            }
            else if ((int)token.charAt(0)>47 && (int)token.charAt(0)<58) {
                num.push(Integer.parseInt(token));
                sPol+=token + " ";
            }
            else {
                char curop = token.charAt(0);
                try {
                    while (priority(op.peek()) >= priority(curop))
                        calc(op.pop());
                }catch (EmptyStackException er){}
                op.push(curop);
            }
        }
        try {
            while (!op.empty())
                calc(op.pop());
        }catch(EmptyStackException er){}

        System.out.print(sPol);
        System.out.println("= "+num.peek());
    }
}
