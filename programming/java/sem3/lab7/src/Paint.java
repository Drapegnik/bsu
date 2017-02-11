import org.w3c.dom.css.RGBColor;

import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.List;

/**
 * Created by Drapegnik on 17.12.15.
 */
public class Paint extends JFrame implements ActionListener {
    private static final int CANVAS_WIDTH = 500;
    private static final int CANVAS_HEIGHT = 300;
    private static Color color = Color.black;
    private JButton btnColor = new JButton("Color");
    private JButton btnOpen = new JButton("Open");
    private JButton btnSaveTXT = new JButton("Save .txt");
    private JButton btnSaveJPG = new JButton("Save .png");
    private List<PolyLine> lines = new ArrayList<>();
    private PolyLine currentLine;
    private DrawCanvas drawPanel;

    public static void main(String[] args) {
        new Paint("Paint");
    }

    public Paint(String title) {
        super(title);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        drawPanel = new DrawCanvas();
        drawPanel.setPreferredSize(new Dimension(CANVAS_WIDTH, CANVAS_HEIGHT));
        drawPanel.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                currentLine = new PolyLine(color);
                lines.add(currentLine);
                currentLine.addPoint(e.getX(), e.getY());
            }
        });
        drawPanel.addMouseMotionListener(new MouseMotionAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                currentLine.addPoint(e.getX(), e.getY());
                repaint();
            }
        });

        Box vertical = new Box(1);
        Box horizontal = new Box(2);
        vertical.add(drawPanel);
        btnColor.addActionListener(this);
        btnOpen.addActionListener(this);
        btnSaveTXT.addActionListener(this);
        btnSaveJPG.addActionListener(this);
        horizontal.add(btnColor);
        horizontal.add(btnOpen);
        horizontal.add(btnSaveJPG);
        horizontal.add(btnSaveTXT);
        vertical.add(new JScrollPane(drawPanel, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED));
        vertical.add(horizontal);
        add(vertical);

        pack();
        setVisible(true);
    }

    public class DrawCanvas extends JPanel {

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            for (PolyLine line : lines) {
                line.draw(g);
            }
            setBackground(Color.white);
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnColor) {
            Color tempColor = JColorChooser.showDialog(this, "Choose a color", color);
            if (tempColor != null)
                color = tempColor;
        } else if (e.getSource() == btnSaveTXT) {
            PrintWriter wr = null;
            try {
                wr = new PrintWriter(GetFile("Text files (.txt)", "txt", false));
                for (PolyLine line : lines) {
                    List<Integer> y = line.getyList();
                    wr.write(y.size() + " ");
                    int i = 0;
                    for (int x : line.getxList()) {
                        wr.write(x + " " + y.get(i) + " ");
                        i++;
                    }
                    wr.write(line.getColor().getRed() + " " + line.getColor().getGreen() + " " + line.getColor().getBlue() + " ");
                }
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this, ex, "Error!", JOptionPane.PLAIN_MESSAGE);
            } catch (NullPointerException ex) {
            } finally {
                if (wr != null)
                    wr.close();
            }
        } else if (e.getSource() == btnOpen) {
            Scanner sc = null;
            try {
                sc = new Scanner(GetFile("Text files (.txt)", "txt", true));
                lines.clear();
                while (sc.hasNext()) {
                    PolyLine templine = new PolyLine(color.black);
                    lines.add(templine);
                    int size = sc.nextInt();
                    for (int i = 0; i < size; i++)
                        templine.addPoint(sc.nextInt(), sc.nextInt());
                    templine.setColor(new Color(sc.nextInt(), sc.nextInt(), sc.nextInt()));
                    // System.out.println(sc.nextInt()+" "+sc.nextInt());
                }
                repaint();
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this, ex, "Error!", JOptionPane.PLAIN_MESSAGE);
            } catch (NullPointerException ex) {
            } finally {
                if (sc != null)
                    sc.close();
            }
        } else if (e.getSource() == btnSaveJPG) {
            BufferedImage im = new BufferedImage(drawPanel.getWidth(), drawPanel.getHeight(), BufferedImage.TYPE_INT_RGB);
            drawPanel.paint(im.getGraphics());
            try {
                ImageIO.write(im, "png", GetFile("Images (.png)", "png", false));
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this, ex, "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        }


    }

    private File GetFile(String filtername, String fileext, Boolean open) {
        JFileChooser chooser = new JFileChooser();
        File workingDirectory = new File(System.getProperty("user.dir"));
        chooser.setCurrentDirectory(workingDirectory);
        if (open) {
            FileNameExtensionFilter filter = new FileNameExtensionFilter(filtername, fileext);
            chooser.setFileFilter(filter);
            if (chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION)
                return chooser.getSelectedFile();
            else
                return null;
        } else {
            if (chooser.showSaveDialog(this) == JFileChooser.APPROVE_OPTION)
                return chooser.getSelectedFile();
            else
                return null;
        }
    }
}
