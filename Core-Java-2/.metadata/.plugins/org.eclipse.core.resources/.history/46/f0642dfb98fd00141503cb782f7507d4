
public class Point {
    public static final int MINIMAL_POINT_X = 0;
    public static final int MAXIMAL_POINT_Y = 10000;
    public static final int MAXIMAL_POINT_X = 10000;
    public static final int MINIMAL_POINT_Y = 0;
    
    private int x;
    private int y;
    
    public Point(int x, int y) {
        this.setX(x);
        this.setY(y);
    }
    
    public int getX() {
        return x;
    }
    
    public void setX(int x) {
        if (x < MINIMAL_POINT_X || x > MAXIMAL_POINT_X) {
            throw new IllegalArgumentException("Argument x has to be between " + 
        MINIMAL_POINT_X + 
        "and " +
        MAXIMAL_POINT_X);
        }
        
        this.x = x;
    }
    
    public int getY() {
        return y;
    }
    
    public void setY(int y) {
        if (y < MINIMAL_POINT_Y || y > MAXIMAL_POINT_Y) {
            throw new IllegalArgumentException("Argument y has to be between " + 
        MINIMAL_POINT_X + 
        "and " +
        MAXIMAL_POINT_X);
        }
        
        this.y = y;
    }
}