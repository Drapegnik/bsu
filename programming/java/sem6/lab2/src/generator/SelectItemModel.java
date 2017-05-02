package generator;

/**
 * Created by Drapegnik on 5/2/17.
 */
public class SelectItemModel {
    private String title;
    private String value;
    private String imagePath;
    private String imageSize;

    public SelectItemModel(String title, String value, String imagePath) {
        this.title = title;
        this.value = value;
        this.imagePath = imagePath;
        this.imageSize = "50px";
    }

    public SelectItemModel(String title, String value, String imagePath, int imageSize) {
        this(title, value, imagePath);
        this.imageSize = imageSize + "px";
    }

    public String getImageSize() {return imageSize;}

    public String getTitle() {return title;}

    public String getValue() {return value;}

    public String getImagePath() {return imagePath;}
}