import javax.swing.*;
import java.awt.*;

public class MainFrame extends JFrame {

    private int radius;

    public static void main(String[] args) {
        new MainFrame(50);
    }

    public MainFrame(int r) {
        super("MainFrame");
        radius = r;
        setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, BoxLayout.Y_AXIS));
        Box b = new Box(1);

        Draw jPanel = new Draw(radius);
        b.add(jPanel);

        container.add(b);
        setBounds(100, 100, 450, 300);

        Thread t1 = new Thread(new FirstThread(jPanel, 6));
        Thread t2 = new Thread(new SecondThread(jPanel, 7));

        t1.start();
        t2.start();

        setVisible(true);
    }
}

class FirstThread implements Runnable {
    private Draw panel;
    private int count;

    public FirstThread(Draw panel, int count) {
        this.panel = panel;
        this.count = count;
    }

    public void run() {
        while (true) {
            if (count == 0)
                break;

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            panel.setRadius(5);
            panel.repaint();
            count--;
        }
        System.out.println("First thread done");
    }
}

class SecondThread implements Runnable {
    private Draw panel;
    private int count;

    public SecondThread(Draw panel, int count) {
        this.panel = panel;
        this.count = count;
    }

    public void run() {
        while (true) {
            if (count == 0)
                break;

            try {
                Thread.sleep(1500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            panel.setRadius(-10);
            panel.repaint();
            count--;
        }
        System.out.println("Second thread done");
    }
}

class Draw extends JPanel {
    private int radius;

    public Draw(int r) {
        this.radius = r;
    }

    public void paint(Graphics g) {
        super.paint(g);
        g.setColor(Color.CYAN);
        g.fillOval(getWidth() / 2 - this.getRadius(), getHeight() / 2 - this.getRadius(), 2 * this.getRadius(), 2 * this.getRadius());
        System.out.println(this.getRadius());
    }

    public synchronized int getRadius() {
        return radius;
    }

    public synchronized void setRadius(int value) {
        this.radius += value;
    }
}
