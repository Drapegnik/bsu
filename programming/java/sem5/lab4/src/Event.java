import java.util.EventObject;

/**
 * Created by Drapegnik on 12.12.16.
 */
public class Event extends EventObject {
   // private static final long serialVersionUID = 1L;
    private int currentIndex;
    private int numberOfSymbols;

    public Event(Object source, int currentIndex, int numberOfSymbols) {
        super(source);
        this.currentIndex = currentIndex;
        this.numberOfSymbols = numberOfSymbols;
    }

    public int getCurrentIndex() {
        return currentIndex;
    }

    public int getNumberOfSymbols() {
        return numberOfSymbols;
    }
}
