import java.util.List;
import java.util.Map;


public class NearestPointFinder extends Thread {
    private List<Point> inPoints;
    private int indexFrom;
    private int indexTo;
    private Map<Point, Point> outMap;
    public NearestPointFinder(
            List<Point> inPoints, 
            int indexFrom, 
            int indexTo, 
            Map<Point, Point> outMap) {
        this.inPoints = inPoints;
        this.indexFrom = indexFrom;
        this.indexTo = indexTo;
        this.outMap = outMap;
              
    }
    
    public void run() {
        PointCalculations.doCalculations(inPoints, indexFrom, indexTo, outMap);
    }
}
