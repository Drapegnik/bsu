import java.io.*;
import java.util.AbstractCollection;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by Drapegnik on 13.11.15.
 */
public class Main {
    public static double x[],a[][];
    public static int n,m,where[];

    public static void gaus() {
        x = new double[n];
        where = new int [n];
//        for (int i = 0; i < n; i++)
//            where[i]=-1;

        Arrays.fill(where,-1);

        for (int col=0, row=0; col < m && row<n; col++) {
            int sel = row;
            for (int i=row; i<n; i++)
                if (Math.abs(a[i][col]) > Math.abs(a[sel][col]))
                    sel = i;

            for (int i=col; i<=m; i++) {
                double temp = a[sel][i];
                a[sel][i] = a[row][i];
                a[row][i] = temp;
            }

            where[col] = row;

            for (int i = 1; i < n; i++)
                if (i!=row) {
                    double c = a[i][col] / a[row][col];
                    for (int j = 0; j <= m; j++)
                        a[i][j] -= a[row][j] * c;
                }
            row++;
        }

        for (int col=0, row=0; col<m; col++) {
            for (int i=0; i<n; i++)
                if (i != row) {
                    double c = a[i][col]/a[row][col];
                    a[i][col] -= a[row][col] * c;
                }
            row++;
        }

        for (int i=0; i<m; i++)
            x[i] = a[i][m] / a[where[i]][i];
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = null;
        PrintWriter wr = null;
        try {
            sc = new Scanner(new FileReader("input.txt"));
            wr = new PrintWriter(new File ("output.txt"));
            n = sc.nextInt();
            m = sc.nextInt();
            a = new double[n][m+1];
            for (int i=0; i<n; i++)
                for (int j=0; j<=m; j++)
                    a[i][j] = sc.nextDouble();

            gaus();

            for (int i=0; i<n; i++) {
                for (int j=0; j<=m; j++)
                    wr.write(a[i][j]+"\t");
                wr.println();
            }

            for (int i=0; i<n; i++)
                System.out.print(x[i]+" ");
        }finally {
            if (sc != null)
                sc.close();
            if (wr != null)
                wr.close();
        }
    }
}
