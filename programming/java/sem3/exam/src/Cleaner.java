/**
 * Created by Drapegnik on 23.12.15.
 */
public class Cleaner {
    private String firm;
    private String color;
    private String inmsrc;
    private int power;

    public Cleaner(String firm, String color, String imgsrc, int power) {
        this.firm = firm;
        this.color = color;
        this.inmsrc = inmsrc;
        this.power = power;
    }

    public String getFirm() {
        return firm;
    }

    public void setFirm(String firm) {
        this.firm = firm;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getInmsrc() {
        return inmsrc;
    }

    public void setInmsrc(String inmsrc) {
        this.inmsrc = inmsrc;
    }

    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }

    @Override
    public String toString() {
        return firm + " " + color + " " + power + " ";
    }
}

