import java.util.ArrayList;
import java.util.List;

/**
 * Created by Drapegnik on 12.12.16.
 */
public class EventSource {
	List<Listener> listeners = new ArrayList<>();
	
	public void addListener(Listener listener) {
		listeners.add(listener);
	}
	
	public void removeListener(Listener listener) {
		listeners.remove(listener);
	}
	
	public void handleEvent(int currentIndex, int numberOfSymbols) {
		Event event = new Event(this, currentIndex, numberOfSymbols);
		for (Listener l: listeners) {
			l.countPercent(event);
		}
	}
}
