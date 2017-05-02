package generator;

import javax.servlet.jsp.tagext.*;
import javax.servlet.jsp.*;
import java.io.*;


/**
 * Created by Drapegnik on 5/1/17.
 */
public class SelectItem extends SimpleTagSupport {
    private String imagePath;
    private String imageSize;
    private String name;
    private String value;
    private boolean isChecked;
    private StringWriter sw = new StringWriter();

    public String getImagePath() {return imagePath;}

    public void setImagePath(String imagePath) {this.imagePath = imagePath;}

    public String getImageSize() {return imageSize;}

    public void setImageSize(String imageSize) {this.imageSize = imageSize;}

    public String getName() {return name;}

    public void setName(String name) {this.name = name;}

    public String getValue() {return value;}

    public void setValue(String value) {this.value = value;}

    public boolean getIsChecked() {return isChecked;}

    public void setIsChecked(boolean checked) {isChecked = checked;}

    public void doTag() throws JspException, IOException {
        String image = "<img src=\"" + imagePath + "\" width=\"" + imageSize + "\">\n";
        String checked = isChecked ? "checked" : "";
        String input = "<input " +
                "type=\"radio\" " +
                "name=\"" + name + "\" " +
                "value=\"" + value + "\" " +
                checked +
                ">\n";
        JspWriter out = getJspContext().getOut();
        getJspBody().invoke(sw);

        out.println("<div class=\"form-group\">\n" +
                "   <div class=\"pull-left\">" + image +
                "       <h3 class=\"pull-right\">" + sw.toString() + "</h3>\n" +
                "   </div>\n" +
                "   <div class=\"pull-right\">\n" +
                "       <label class=\"btn btn-default btn-circle btn-lg\">\n" +
                "          " + input +
                "          <i class=\"glyphicon glyphicon-ok\"></i>\n" +
                "      </label>\n" +
                "   </div>\n" +
                "</div>\n");
    }
}