package CourseTasks;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class PointCalculations {
	private static Random rnd = new Random();
	private static final int NUMBER_OF_POINTS = 100000;

	public static void main(String[] args) throws InterruptedException {
		long startTime = System.currentTimeMillis();

		List<Point> points = generatePoints();
		// Map<Point, Point> nearestPoints = getNearestPoints(points);
		// Execution of the one thread code above took 161 754 milliseconds

		Map<Point, Point> outMap = new HashMap<Point, Point>();

		NearestPointFinder finderOne = new NearestPointFinder(points, 0, 6667,
				outMap);
		NearestPointFinder finderTwo = new NearestPointFinder(points, 6667,
				13334, outMap);
		NearestPointFinder finderThree = new NearestPointFinder(points, 13334,
				20001, outMap);
		NearestPointFinder finderFour = new NearestPointFinder(points, 20001,
				26668, outMap);
		NearestPointFinder finderFive = new NearestPointFinder(points, 28751,
				35714, outMap);
		NearestPointFinder finderSix = new NearestPointFinder(points, 35714,
				42857, outMap);
		NearestPointFinder finderSeven = new NearestPointFinder(points, 42857,
				50000, outMap);
		NearestPointFinder finderEight = new NearestPointFinder(points, 50000,
				57143, outMap);
		NearestPointFinder finderNine = new NearestPointFinder(points, 57143,
				64286, outMap);
		NearestPointFinder finderTen = new NearestPointFinder(points, 64286,
				71429, outMap);
		NearestPointFinder finderEleven = new NearestPointFinder(points, 71429,
				78572, outMap);
		NearestPointFinder finderTwelve = new NearestPointFinder(points, 78572,
				85715, outMap);
		NearestPointFinder finderThirteen = new NearestPointFinder(points,
				85715, 92858, outMap);
		NearestPointFinder finderFourteen = new NearestPointFinder(points,
				92858, 100000, outMap);

		finderOne.start();
		finderTwo.start();
		finderThree.start();
		finderFour.start();
		finderFive.start();
		finderSix.start();
		finderSeven.start();
		finderEight.start();
		finderNine.start();
		finderTen.start();
		finderEleven.start();
		finderTwelve.start();
		finderThirteen.start();
		finderFourteen.start();

		finderOne.join();
		finderTwo.join();
		finderThree.join();
		finderFour.join();
		finderFive.join();
		finderSix.join();
		finderSeven.join();
		finderEight.join();
		finderNine.join();
		finderTen.join();
		finderEleven.join();
		finderTwelve.join();
		finderThirteen.join();
		finderFourteen.join();

		long endTime = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println(totalTime);
		System.out.println(outMap.size());

	}

	public static List<Point> generatePoints() {
		List<Point> points = new ArrayList<Point>();

		for (int i = 0; i < NUMBER_OF_POINTS; i++) {
			Point point = new Point(rnd.nextInt(Point.MAXIMAL_POINT_X + 1),
					rnd.nextInt(Point.MAXIMAL_POINT_Y + 1));
			points.add(point);
		}

		return points;
	}

	public static Map<Point, Point> getNearestPoints(List<Point> points) {
		Map<Point, Point> nearestPoints = new HashMap<Point, Point>();
		int length = points.size();

		Point point = null;
		Point nearestPoint = null;
		Point pointToCheck = null;

		for (int i = 0; i < length; i++) {
			double minDistance = Double.MAX_VALUE;
			point = points.get(i);
			for (int j = 0; j < length; j++) {
				pointToCheck = points.get(j);
				if (j == i) {
					continue;
				}

				double distance = calculateDistance(point, pointToCheck);
				if (distance < minDistance) {
					minDistance = distance;
					nearestPoint = pointToCheck;
				}
			}

			nearestPoints.put(point, nearestPoint);
		}

		return nearestPoints;
	}

	public static void doCalculations(List<Point> inPoints, int indexFrom,
			int indexTo, Map<Point, Point> outMap) {
		Point point = null;
		Point nearestPoint = null;
		Point pointToCheck = null;

		for (int i = indexFrom; i < indexTo; i++) {
			double minDistance = Double.MAX_VALUE;
			point = inPoints.get(i);
			for (int j = indexFrom; j < indexTo; j++) {
				pointToCheck = inPoints.get(j);
				if (j == i) {
					continue;
				}

				double distance = calculateDistance(point, pointToCheck);
				if (distance < minDistance) {
					minDistance = distance;
					nearestPoint = pointToCheck;
				}
			}

			synchronized (outMap) {
				outMap.put(point, nearestPoint);
			}
		}
	}

	private static double calculateDistance(Point pointA, Point pointB) {
		double distance = Math
				.sqrt(Math.pow((pointA.getX() - pointB.getX()), 2)
						+ Math.pow((pointA.getY() - pointB.getY()), 2));

		return distance;
	}
}
