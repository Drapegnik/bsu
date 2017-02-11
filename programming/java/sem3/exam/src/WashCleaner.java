/**
 * Created by Drapegnik on 21.12.15.
 */
public class WashCleaner extends Cleaner{
    private int capacity;

    public WashCleaner(String firm, String color, String imgsrc, int power, int capacity) {
        super(firm, color, imgsrc, power);
        this.capacity = capacity;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    @Override
    public String toString() {
        return super.toString()+capacity;
    }
}
