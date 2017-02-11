/**
 * Created by Drapegnik on 21.12.15.
 */
public class RobotCleaner extends Cleaner {
    private Boolean isHaveScreen;

    public RobotCleaner(String firm, String color, String imgsrc, int power,Boolean isHaveScreen) {
        super(firm,color,imgsrc,power);
        this.isHaveScreen = isHaveScreen;
    }

    public Boolean getIsHaveScreen() {
        return isHaveScreen;
    }

    public void setIsHaveScreen(Boolean isHaveScreen) {
        this.isHaveScreen = isHaveScreen;
    }

    @Override
    public String toString() {
        return super.toString()+isHaveScreen;
    }
}
