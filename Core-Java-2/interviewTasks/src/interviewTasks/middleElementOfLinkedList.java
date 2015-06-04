package interviewTasks;

import java.util.Arrays;
import java.util.LinkedList;

public class middleElementOfLinkedList {

	static <T> T getMiddleElement(LinkedList<T> linkedListWithIntegers) {
		LinkedList<T> rabit = new LinkedList<>(linkedListWithIntegers);
		LinkedList<T> turtle = new LinkedList<>(linkedListWithIntegers) ;
		int rabitInt = 0;
		T mid = turtle.getFirst();
		while (!rabit.isEmpty()) {
			rabit.remove();
			rabitInt++;
			if (rabitInt % 2 == 1) {
				mid = turtle.poll();

			}
		}
		return mid;
	}

	public static void main(String[] args) {
		LinkedList<Integer> linkedListWithIntegers = new LinkedList<Integer>(
				Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13));
		System.out.println(Arrays.toString(linkedListWithIntegers.toArray()));
		System.out.println(getMiddleElement(linkedListWithIntegers));
	}
}