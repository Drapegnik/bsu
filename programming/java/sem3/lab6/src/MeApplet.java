import javax.swing.*;
import java.awt.event.*;

/**
 * Created by Drapegnik on 11.12.15.
 */
public class MeApplet extends JApplet {
    private JButton btn = new JButton("Click me!");

    public void init() {
        setLayout(null);
        btn.setSize(100, 100);
        add(btn);

        btn.addMouseMotionListener(new MouseAdapter() {
            private int x, y;

            @Override
            public void mouseMoved(MouseEvent e) {
                x = e.getX();
                y = e.getY();
                showStatus("x: " + e.getX() + " y:" + e.getY());
            }

            @Override
            public void mouseDragged(MouseEvent e) {
                if (e.isControlDown()) {
                    btn.setLocation(btn.getX() + e.getX() - x, btn.getY() + e.getY() - y);
                    showStatus("x: " + (e.getX() + btn.getX()) + ", y: " + (e.getY() + btn.getY()));
                }
            }
        });

        btn.addKeyListener(new KeyAdapter() {
            @Override
            public void keyTyped(KeyEvent e) {
                if (e.getKeyChar() == KeyEvent.VK_BACK_SPACE) {
                    if (btn.getText().length() > 0)
                        btn.setText(btn.getText().substring(0, btn.getText().length() - 1));
                } else
                    btn.setText(btn.getText() + Character.toString(e.getKeyChar()));
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseMoved(MouseEvent e) {
                showStatus("x: " + e.getX() + " y:" + e.getY());
            }
        });

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                btn.setLocation(e.getX(), e.getY());
            }
        });
    }
}

